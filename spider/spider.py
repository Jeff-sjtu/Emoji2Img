import requests
import re
import json

keywords = []
with file("keywords.txt") as f:
    keywords = f.readlines()
keywords = [d.strip() for d in keywords]


while(True):
    temp = requests.get('http://www.doutula.com/so/init').json()
    print temp['hot'].values()
    temp2 = [d['keyword'] for d in temp['hot'].values()]
    for d in temp['realtime']:
        if not d['keyword'] in temp2:
            temp2.append(d['keyword'])
    for d in temp2:
        if not d in keywords:
            keywords.append(d)
            temp = requests.get('http://www.doutula.com/search?keyword='+d)
            print temp.text
            raw_input()
