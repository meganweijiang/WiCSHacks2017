import json
import re
from watson_developer_cloud import ToneAnalyzerV3
from app.gettweets import *

tone_analyzer = ToneAnalyzerV3(
    username='a82107db-ddfd-4d75-b2a8-6addabe05a47',
    password='pKJ1lho7jQ2o',
    version='2016-02-11')

def getTones(jsonList):
	toneList = []
	for item in jsonList:
		clean_tweet = re.sub(r"(?:\@|https?\://)\S+", "", item)
		clean_tweet = re.sub("RT", "", clean_tweet)
		toneList.append(tone_analyzer.tone(text=clean_tweet)['document_tone']['tone_categories'][0]['tones'])
	return toneList

def getAvg(toneList):
	length = len(toneList)

	averages = {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.0}

	angerTotal = 0.0
	disgustTotal = 0.0
	fearTotal = 0.0
	joyTotal = 0.0
	sadnessTotal = 0.0

	for item in toneList:
		angerTotal += float(item[0]['score'])
		disgustTotal += float(item[1]['score'])
		fearTotal += float(item[2]['score'])
		joyTotal += float(item[3]['score'])
		sadnessTotal += float(item[4]['score'])

	try:
		averages['anger'] = float(angerTotal / length)
		averages['disgust'] = float(disgustTotal / length)
		averages['fear'] = float(fearTotal / length)
		averages['joy'] = float(joyTotal / length)
		averages['sadness'] = float(sadnessTotal / length)
	except ZeroDivisionError as err:
		print (err)

	return averages
