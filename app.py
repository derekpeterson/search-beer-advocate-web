from flask import Flask, redirect, render_template, request, url_for
import requests
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = []
    if query:
        return render_template('search.html', query=query, results=results)
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug = True)
