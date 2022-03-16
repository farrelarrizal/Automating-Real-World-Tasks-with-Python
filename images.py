
#!usr/bin/env python3
from PIL import Image
import os

path = '../../home/<username>/images/'
imagesDir = os.listdir(path)

for image in imagesDir:
    if image == '.DS_Store':
        continue
    else:
        Image.open(path+image).convert('RGB').rotate(-90).resize((128, 128)).save(image, 'jpeg')