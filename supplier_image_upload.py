#!/usr/bin/env python3
import requests
import os

url = 'http://localhost/upload/'

for thing in os.listdir('./supplier-data/images/'):
  if thing.endswith('.jpeg'):
    file = '/home/student-00-e70fad3680b2/supplier-data/images/' + thing
    with open (file=file, mode='rb') as opened:
      r = requests.post(url=url, files={'file': opened})
  else:
    continue