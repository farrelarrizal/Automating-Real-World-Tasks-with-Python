#!/usr/bin/env python3

import os
from PIL import Image

path = './supplier-data/images/'
imagesDir = os.listdir(path)

for image in imagesDir:
    if image.endswith('tiff'):
        new_name = image.split('.')
        Image.open(path+image).convert('RGB').resize((600, 400)).save(path+new_name[0]+'.jpeg', 'JPEG')
    else:
        continue
