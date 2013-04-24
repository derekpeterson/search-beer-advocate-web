from flask import Flask, redirect, render_template, request, url_for
from flask.ext.cacheify import init_cacheify
import json
import re
import requests
app = Flask(__name__)
cache = init_cacheify(app)

from app import cache

CLEAN = re.compile(r'<[^<]*?/?>|[\';:]')
DIGIT = re.compile(r'^\d{3}')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    query = CLEAN.sub('', query)
    text = cache.get(query)
    if not text or DIGIT.match(text):
        r = requests.get(
            'http://ec2-54-245-176-209.us-west-2.compute.amazonaws.com:8080?q='
            + query)
        cache.set(query, r.text, 86400)
        text = r.text
    text = text.split('\n////\n')
    results = []
    for line in text:
        if line == '' or DIGIT.match(line):
            continue
        beer = json.loads(re.sub(r"\n+|\||\t+", ' ', line))
        results.append(beer)
    return render_template('search.html', query=query, results=results, count=len(results))

@app.route('/feedback')
def feedback():
    item = request.args.get('id', '')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run()
