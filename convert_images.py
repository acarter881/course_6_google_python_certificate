#!/usr/bin/env python3
import os
from PIL import Image

for infile in os.listdir('./images'):
  if infile.startswith('.'):
    continue
  else:
    with Image.open(fp='/home/student-00-8d904407f783/images/' + infile) as im:
      im = im.convert('RGB')
      im.rotate(angle=-90).resize(size=((128, 128))).save(fp='/opt/icons/' + infile, format='jpeg')
