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
	return render_template('search.html', data=json.dumps(vals))

if __name__ == "__main__":
    app.run(debug=True)