import json
from watson_developer_cloud import ToneAnalyzerV3
from gettweets import *

toneList = []
averages = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None}

angerTotal = 0.0
disgustTotal = 0.0
fearTotal = 0.0
joyTotal = 0.0
sadnessTotal = 0.0

tone_analyzer = ToneAnalyzerV3(
    username='a82107db-ddfd-4d75-b2a8-6addabe05a47',
    password='pKJ1lho7jQ2o',
    version='2016-02-11')

api_inst = getInst()
getData(api_inst)

for item in jsonList:
	toneList.append(tone_analyzer.tone(text=item)['document_tone']['tone_categories'][0]['tones'])

for item in toneList:
	angerTotal += float(item[0]['score'])
	disgustTotal += float(item[1]['score'])
	fearTotal += float(item[2]['score'])
	joyTotal += float(item[3]['score'])
	sadnessTotal += float(item[4]['score'])

averages['anger'] = float(angerTotal / length)
averages['disgust'] = float(disgustTotal / length)
averages['fear'] = float(fearTotal / length)
averages['joy'] = float(joyTotal / length)
averages['sadness'] = float(sadnessTotal / length)

print (averages)