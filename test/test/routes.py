from test import app
from test.models import Book
from flask import render_template, send_from_directory

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)
