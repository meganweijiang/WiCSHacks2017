#!flask/bin/python

from flask import Flask, render_template, request, redirect, url_for
from app.gettweets import *
from app.getemotions import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Megan and Tiffany"
    name = "WiCS Hacks 2017"
    return render_template('index.html', author=author, name=name)

@app.route('/search', methods=['GET'])
def search():
	name = "WiCS Hacks 2017"
	twitter_query = request.args.get('search_query')
	api_inst = getInst()
	getData(api_inst, twitter_query)
	getTones(jsonList)
	vals = getAvg(toneList)
	anger = vals['anger']
	disgust = vals['disgust']
	fear = vals['fear']
	joy = vals['joy']
	sadness = vals['sadness']
	return render_template('search.html', name=name, anger=anger, disgust=disgust, fear=fear, joy=joy, sadness=sadness)

if __name__ == "__main__":
    app.run(debug=True)