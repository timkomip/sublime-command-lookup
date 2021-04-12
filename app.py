from flask import Flask, render_template, request
from data import get_searcher

app = Flask(__name__)

@app.route('/')
def home():
    query = request.args.get('query', '')
    commands = get_searcher().search(query)
    return render_template('home.html', commands=commands, query=query)

