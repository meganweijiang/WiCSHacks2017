import json
import tweepy
import os

API_KEY = os.environ.get('TWITTER_API_KEY')
API_SECRET = os.environ.get('TWITTER_API_SECRET')
TOKEN_KEY = os.environ.get('TWITTER_TOKEN')
TOKEN_SECRET = os.environ.get('TWITTER_SECRET')

def store(tweet, jsonList):
	jsonList.append(json.dumps(tweet))

def getInst():
	auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
	auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
	api_inst = tweepy.API(auth)
	return api_inst

def getData(api_inst, twitter_query):
	jsonList = []
	counter = 0
	try:
		twitter_cursor = tweepy.Cursor(api_inst.search, q=twitter_query, lang="en")
		for page in twitter_cursor.pages():
			if counter == 50:
				break
			for item in page:
				if counter == 50:
					break
				else:
					store(item.text, jsonList)
					counter += 1
	except tweepy.error.TweepError as err:
		print (err)

	return jsonList
