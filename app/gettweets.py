import json
import tweepy

API_KEY = 'ypOZYLGlzL83c8RcG0vkUIJ6Y'
API_SECRET = '60V0stdGQf6KYveJ6jpb33y9lFAw2sHYuGa9IZvSCjm70cciSH'
TOKEN_KEY = '803397824822083584-0J6i6wpp6KdGqZPIexlAVdGs6MhPNCp'
TOKEN_SECRET = 'twwHBypmQrnFPS0JiS3tHvNJUJ5px1LEvgKooYBaHNm9F'

jsonList = []

def store(tweet):
  jsonList.append(json.dumps(tweet))

def getInst():
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
  api_inst = tweepy.API(auth)
  return api_inst

def getData(api_inst):
  counter = 0
  twitter_query = input("enter query: ")
  twitter_cursor = tweepy.Cursor(api_inst.search, q=twitter_query, lang="en")
  for page in twitter_cursor.pages():
    for item in page:
      if counter == 100:
        break
      else:
        store(item.text)
        counter += 1
