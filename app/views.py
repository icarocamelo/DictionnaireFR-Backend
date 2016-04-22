from flask import request
from app import app
from HTMLParser import HTMLParser


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/search')
def search():
    term = request.args.get('term')
    parser = HTMLParser()
    result = parser.parse(term)

    return result
