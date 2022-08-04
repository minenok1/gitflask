

from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello():
    return '<h1>Hello, Github!</h1>'


@app.route('/about/')
def about():
    return '<h3>About page that will explain u some things</h3>'
