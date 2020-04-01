from flask import Flask,render_template,g
import sqlite3

DATABASE = "./Data.sqlite3"
DEBUG = True

app = Flask(__name__)

@app.route('/')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.after_request
def after_request(response):
    g.db.close()
    return response

def hello():
    html = render_template('index.html',a = '20-0401 16:00',b = '2768',c = '双日',d = '267')
    return html

if __name__ == "__main__":
    app.run(debug= True)