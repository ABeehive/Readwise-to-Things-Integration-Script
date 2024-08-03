import requests
import webbrowser
from urllib.parse import quote

# Set your Readwise API token
READWISE_API_TOKEN = 'READWISE_API_TOKEN' #You can get that from here: readwise.io/access_token
ACTIONABLE_HIGHLIGHT = 'i' # Set this to what you tag your highlights so you want them included in Things 3

# Function to fetch all highlights from Readwise
def fetch_highlights():
    url = 'https://readwise.io/api/v2/highlights/'
    headers = {
        'Authorization': f'Token {READWISE_API_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['results']

# Function to fetch book details by book_id
def fetch_book_details(book_id):
    url = f'https://readwise.io/api/v2/books/{book_id}/'
    headers = {
        'Authorization': f'Token {READWISE_API_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

# Function to filter highlights by tag
def filter_highlights_by_tag(highlights, tag):
    return [highlight for highlight in highlights if any(t['name'] == tag for t in highlight['tags'])]

# Function to create tasks in Things
def create_task_in_things(title, highlight, note):
    encoded_title = quote(f'⭕️ {title}')
    encoded_notes = quote(f'{highlight}\n{note}')
    url = f'things:///add?title={encoded_title}&notes={encoded_notes}'
    webbrowser.open(url)

# Function to delete a tag from a highlight
def delete_tag_from_highlight(highlight_id, tag_id):
    url = f'https://readwise.io/api/v2/highlights/{highlight_id}/tags/{tag_id}/'
    headers = {
        'Authorization': f'Token {READWISE_API_TOKEN}'
    }
    response = requests.delete(url, headers=headers)
    response.raise_for_status()

# Main function to process highlights and create tasks
def main():
    highlights = fetch_highlights()
    filtered_highlights = filter_highlights_by_tag(highlights, ACTIONABLE_HIGHLIGHT)
    
    for highlight in filtered_highlights:
        # Print the highlight keys for debugging
        print(highlight.keys())
        
        # Fetch the book details
        book_id = highlight.get('book_id')
        book_details = fetch_book_details(book_id)
        book_title = book_details.get('title', 'Unknown Title')
        
        highlight_text = highlight.get('text', 'No Highlight Text')
        note = highlight.get('note', '')
        
        create_task_in_things(book_title, highlight_text, note)
        
        # Delete the tag from the highlight
        highlight_id = highlight.get('id')
        tag_id = next(tag['id'] for tag in highlight['tags'] if tag['name'] == ACTIONABLE_HIGHLIGHT)
        delete_tag_from_highlight(highlight_id, tag_id)

if __name__ == '__main__':
    main()
