from flask import Flask, render_template, request

app = Flask(__name__)

# Define the flag
FLAG = "CTF{your_flag_here}"

# Sample book data
books = {
    1: "Introduction to Python",
    2: "Web Development with Flask",
    3: "Machine Learning Basics",
    # Add more books as needed
}

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def view_book(book_id):
    # Check for IDOR vulnerability
    if book_id == 59:
        return f"Flag: {FLAG}"
    else:
        # Display book information
        book_title = books.get(book_id, "Book not found")
        return f"Book ID: {book_id}, Title: {book_title}"

if __name__ == '__main__':
    app.run(debug=True)
