#! /usr/bin/env python3

import os
import requests

url = 'http://35.193.9.85/fruits/'
keys = ['name', 'weight', 'description', 'image_name']
path = './supplier-data/descriptions/'

image = 1
for file in os.listdir(path):
    temp = {}
    counter = 0
    with open(path+file) as text:
        for line in text:
            word = line.strip()
            if word.endswith('lbs'):
                word = word.split(' ')
                word = word[0]
                word = int(word)
            temp[keys[counter]] = word
            if image < 10:
                temp['image_name'] = '00'+str(image)+'.jpeg'
            else:
                temp['image_name'] = '0'+str(image)+'.jpeg'
            counter += 1
        image += 1
    response = requests.post(url, json=temp)
    print(response.status_code)
