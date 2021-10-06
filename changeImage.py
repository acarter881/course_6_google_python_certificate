#!/usr/bin/env python3
import os
from PIL import Image

for infile in os.listdir('./supplier-data/images/'):
  if infile.endswith('.tiff'):
    with Image.open(fp='/home/student-00-e70fad3680b2/supplier-data/images/' + infile) as im:
      im = im.convert('RGB')
      infile = infile.split('.')[0] + '.jpeg'
      im.resize(size=((600, 400))).save(fp='/home/student-00-e70fad3680b2/supplier-data/images/' + infile, format='jpeg')
  else:
    continue