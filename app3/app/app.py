from typing import List, Dict
from flask import Flask
import mysql.connector
import json
from flask_migrate import Migrate
from app.models import Book
from flask import render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
migrate = Migrate(app, db)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hard to guess'
#UPLOAD_FOLDER = 'uploads'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

from app import models

#def test_table() -> List[Dict]:
   # config = {
    #    'user': 'root',
    #    'password': 'root',
    #    'host': 'db',
   #     'port': '3306',
   #     'database': 'devopsroles'
   # }
   # connection = mysql.connector.connect(**config)
   # cursor = connection.cursor()
   # cursor.execute('SELECT * FROM test_table')
    #results = [{name: color} for (name, color) in cursor]
   # cursor.close()
   # connection.close()

    #return results


#@app.route('/')
#def index() -> str:
 #   return json.dumps({'test_table': test_table()})

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

from app import routes, models
