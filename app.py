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
    results = [{
        'id': i,
        'url': url_for('index'),
        'name': "Beer Ipsum IPA",
        'summary': "Brew kettle noble hops aerobic, abv bock dry hopping craft beer. squares krug hefe mash mash tun bitter lauter; cask conditioned ale aau barley dry stout. degrees plato hydrometer goblet conditioning tank craft beer biere de garde becher. lauter tun; malt extract ibu berliner weisse degrees plato. bunghole bottom fermenting yeast amber bunghole enzymes lauter; bitter. alpha acid aerobic malt double bock/dopplebock. bottom fermenting yeast attenuation, units of bitterness caramel malt. kolsch squares wort saccharification pint glass, amber biere de garde."
    } for i in range(20)]
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
