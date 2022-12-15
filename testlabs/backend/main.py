from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "<h1>Hello, World from Antananarivo!<h1>"

if __name__ == '__main__':
   app.run(host='0.0.0.0')


config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }
connection = mysql.connector.connect(**config)
