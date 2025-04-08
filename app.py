import streamlit as st
import pandas as pd
from datetime import datetime
import json
import os

# Set page configuration
st.set_page_config(
    page_title="Personal Library Manager",
    page_icon="📚",
    layout="wide"
)

# Initialize session state for the library
if 'library' not in st.session_state:
    if os.path.exists('library.json'):
        with open('library.json', 'r') as f:
            st.session_state.library = json.load(f)
    else:
        st.session_state.library = []

def save_library():
    with open('library.json', 'w') as f:
        json.dump(st.session_state.library, f)

# Main title
st.title("📚 Personal Library Manager")

# Sidebar for adding new books
with st.sidebar:
    st.header("Add New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Science", "Technology", "History", "Biography", "Other"])
    isbn = st.text_input("ISBN (optional)")
    publication_year = st.number_input("Publication Year", min_value=1000, max_value=datetime.now().year, value=2024)
    status = st.selectbox("Reading Status", ["Unread", "Currently Reading", "Completed"])
    rating = st.slider("Rating", 0, 5, 0)
    notes = st.text_area("Notes")

    if st.button("Add Book"):
        if title and author:  # Basic validation
            new_book = {
                "title": title,
                "author": author,
                "genre": genre,
                "isbn": isbn,
                "publication_year": publication_year,
                "status": status,
                "rating": rating,
                "notes": notes,
                "date_added": datetime.now().strftime("%Y-%m-%d")
            }
            st.session_state.library.append(new_book)
            save_library()
            st.success("Book added successfully!")
        else:
            st.error("Title and Author are required!")

# Main content area
tab1, tab2, tab3 = st.tabs(["📚 Library", "📊 Statistics", "🔍 Search"])

with tab1:
    if not st.session_state.library:
        st.info("Your library is empty. Add some books using the sidebar!")
    else:
        # Convert library to DataFrame for better display
        df = pd.DataFrame(st.session_state.library)
        
        # Add delete button functionality
        for idx, book in enumerate(st.session_state.library):
            col1, col2, col3 = st.columns([0.7, 0.2, 0.1])
            with col1:
                st.write(f"**{book['title']}** by {book['author']}")
                st.write(f"Genre: {book['genre']} | Status: {book['status']} | Rating: {'⭐' * book['rating']}")
            with col2:
                if st.button("🖋️", key=f"edit_{idx}"):
                    st.session_state.editing_index = idx
            with col3:
                if st.button("🗑️", key=f"delete_{idx}"):
                    st.session_state.library.pop(idx)
                    save_library()
                    st.rerun()
            st.divider()

with tab2:
    if st.session_state.library:
        df = pd.DataFrame(st.session_state.library)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Books by Genre")
            genre_counts = df['genre'].value_counts()
            st.bar_chart(genre_counts)
            
        with col2:
            st.subheader("Reading Status")
            status_counts = df['status'].value_counts()
            st.bar_chart(status_counts)
            
        st.subheader("Reading Statistics")
        col3, col4, col5 = st.columns(3)
        with col3:
            st.metric("Total Books", len(df))
        with col4:
            completed = len(df[df['status'] == 'Completed'])
            st.metric("Books Completed", completed)
        with col5:
            average_rating = df['rating'].mean()
            st.metric("Average Rating", f"{average_rating:.1f} ⭐")

with tab3:
    search_term = st.text_input("Search books by title, author, or genre")
    if search_term:
        results = []
        for book in st.session_state.library:
            if (search_term.lower() in book['title'].lower() or 
                search_term.lower() in book['author'].lower() or 
                search_term.lower() in book['genre'].lower()):
                results.append(book)
        
        if results:
            st.write(f"Found {len(results)} results:")
            for book in results:
                st.write(f"**{book['title']}** by {book['author']}")
                st.write(f"Genre: {book['genre']} | Status: {book['status']} | Rating: {'⭐' * book['rating']}")
                st.divider()
        else:
            st.info("No books found matching your search terms.") 
