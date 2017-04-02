#!flask/bin/python

from flask import Flask, render_template, request, redirect, url_for
from app.gettweets import *
from app.getemotions import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Megan Weijiang & Tiffany Tso"
    name = "TwitterMood"
    return render_template('index.html', author=author, name=name)

@app.route('/search', methods=['GET'])
def search():
	name = "Results"
	twitter_query = request.args.get('search_query')
	api_inst = getInst()
	jsonList = getData(api_inst, twitter_query)
	toneList = getTones(jsonList)
	vals = getAvg(toneList)
	return render_template('search.html', data=json.dumps(vals), name=name)

@app.route('/about', methods=['GET'])
def about():
	name = "About"
	return render_template('about.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)