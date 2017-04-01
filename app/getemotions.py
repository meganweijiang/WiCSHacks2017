import json
from watson_developer_cloud import ToneAnalyzerV3
from gettweets import *

toneList = []

tone_analyzer = ToneAnalyzerV3(
    username='a82107db-ddfd-4d75-b2a8-6addabe05a47',
    password='pKJ1lho7jQ2o',
    version='2016-02-11')

api_inst = getInst()
getData(api_inst)
print (jsonList)

for item in jsonList:
	toneList.append(tone_analyzer.tone(text=item)['document_tone']['tone_categories'][0]['tones'])

print (toneList)