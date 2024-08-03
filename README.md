# Readwise-to-Things-Integration-Script
This script fetches highlights from Readwise, filters them by a specific tag, and creates tasks in the Things 3 app that match a specific tag. In this way you can create actionable highlights. The task in things has as the title '⭕️ [TITLE OF DOCUMENT]' and in the notes it has the highlight that is considered actionable. Afterwards it removes the specified tag from the processed highlights.

## Prerequisites

- Python 3.x
- `requests` library (install via `pip install requests`)
- Things 3 app installed on your macOS device → https://culturedcode.com/things/ 
- You need to enable the Things URL Scheme : https://culturedcode.com/things/support/articles/2803573/

## Setup

1. **Clone the repository or download the script file.**

2. **Install the required Python package:**
   ```bash
   pip install requests
   ```

3. **Set your Readwise API token:**
   Replace the placeholder `READWISE_API_TOKEN` in the script with your actual Readwise API token.

4. **Set your Actionable Highlight Tag**
   Replace the placeholder 'i', which is what I use for actionable highlights.

## Usage

1. **Run the script:**
   ```zsh
   python3 Readwise-to-Things-Integration-Script.py
   ```

2. The script will:
   - Fetch all highlights from Readwise.
   - Filter highlights tagged with 'i' which is what I use for actionable highlights, the 'i' for 'inbox'. but this will use the user defined ```ACTIONABLE_HIGHLIGHT```
   - Create tasks in the Things app for each filtered highlight.
   - Remove the 'i' tag from the processed highlights.

## Script Details

- **fetch_highlights()**: Fetches all highlights from Readwise.
- **fetch_book_details(book_id)**: Fetches book details by `book_id`.
- **filter_highlights_by_tag(highlights, tag)**: Filters highlights by a specified tag.
- **create_task_in_things(title, highlight, note)**: Creates a task in the Things app.
- **delete_tag_from_highlight(highlight_id, tag_id)**: Deletes a specified tag from a highlight.

## Example

When you run the script, it will:
- Retrieve all highlights from your Readwise account.
- Filter highlights that have the user defined ```ACTIONALBE_HIGHLIGHT```.
- For each filtered highlight, create a task in the Things app with the highlight text and note. 

It creates the task as follows : 
```
title of the task : ⭕️ {title of the source of the highlight, so the book title or article title}
note of the task : the highlight
.the ```ACTIONALBE_HIGHLIGHT``` tag
```


- Remove the ```ACTIONALBE_HIGHLIGHT``` tag from the processed highlight.

## Notes

- Ensure your Readwise API token is kept secure and not shared.
- This script opens URLs in the Things app using the `webbrowser` module, which should be installed by default with Python. 

## License

This project is not licensed. Just have fun with it.

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk. Ensure you understand what the script does before running it. 
**Make sure to TEST run it, as it deletes a tag as well**
