from flask import request
from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/search')
def search():
    term = request.args.get('term')
    # TODO: Call HTML parser
    return "Are you looking for " + term + " ?"
