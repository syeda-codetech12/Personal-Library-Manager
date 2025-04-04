# Personal Library Manager

A Streamlit-based application to manage your personal book collection.

## Features

- Add books with details (title, author, genre, ISBN, etc.)
- View your entire library
- Track reading status and ratings
- Search functionality
- Visual statistics and insights
- Data persistence using JSON storage

## Setup Instructions

1. Make sure you have Python 3.7+ installed on your system.

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. **Adding Books**:
   - Use the sidebar form to add new books
   - Fill in the required fields (Title and Author are mandatory)
   - Click "Add Book" to save

2. **Viewing Library**:
   - Navigate to the "Library" tab to see all your books
   - Each book entry shows title, author, genre, status, and rating
   - Use the delete button to remove books

3. **Statistics**:
   - Check the "Statistics" tab for visual insights
   - View distribution of books by genre and reading status
   - See key metrics like total books and average rating

4. **Searching**:
   - Use the "Search" tab to find specific books
   - Search by title, author, or genre
   - Results update in real-time as you type

## Data Storage

The application stores your library data in a `library.json` file in the same directory. This ensures your data persists between sessions. 