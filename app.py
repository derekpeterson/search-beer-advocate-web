from flask import Flask, redirect, render_template, request, url_for
import json
import re
import requests
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    r = requests.get('http://ec2-54-245-176-209.us-west-2.compute.amazonaws.com:8080?q=' + query)
    results = []
    text = r.text.split('\n////\n')
    for line in text:
        if line == '':
            continue
        beer = json.loads(re.sub(r"\n+|\||\t+", ' ', line))
        results.append(beer)
    return render_template('search.html', query=query, results=results)

@app.route('/feedback')
def feedback():
    item = request.args.get('id', '')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run()
