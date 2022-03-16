#! /usr/bin/env python3
import requests
import os

url = 'http://35.193.9.85/upload/'
path = './supplier-data/images/'

imagesDir = os.listdir(path)

for image in imagesDir:
    if image.endswith('jpeg'):
        with open(path+image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
    else:
        continue
