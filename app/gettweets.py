import json
import tweepy

#API_KEY = 'ypOZYLGlzL83c8RcG0vkUIJ6Y'
#API_SECRET = '60V0stdGQf6KYveJ6jpb33y9lFAw2sHYuGa9IZvSCjm70cciSH'
#TOKEN_KEY = '803397824822083584-0J6i6wpp6KdGqZPIexlAVdGs6MhPNCp'
#TOKEN_SECRET = 'twwHBypmQrnFPS0JiS3tHvNJUJ5px1LEvgKooYBaHNm9F'

API_KEY = 'HJIj9KVlhARSZFwG7CCSjqwOS'
API_SECRET = 'JdfdIVeSNLFuazbzSZeKAofdy7s5IzLVpI25RgjOzOuOreONtT'
TOKEN_KEY = '3243742999-ItaCs47Neu3ve4dTJpcsVz4xvYuJxBSYbrzTRa0'
TOKEN_SECRET = 'mArLXKMpbWArgRRI8UQqYrbJWbZyQxTXmgaMeh9J19CEm'

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
					print("Found a tweet")
	except tweepy.error.TweepError as err:
		print (err)

	return jsonList