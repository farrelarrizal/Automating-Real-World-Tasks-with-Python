#! /usr/bin/env python3

import os
import requests

keys = ['title', 'name', 'date', 'feedback']
path = '/data/feedback/'

for file in os.listdir(path):
    temp = {}
    counter = 0
    with open(path+file) as text:
        for line in text:
            word = line.strip()
            temp[keys[counter]] = word
            counter += 1
    response = requests.post('http://35.202.217.187/feedback/', json=temp)
    print(temp)
print(response.status_code)
