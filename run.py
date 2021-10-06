#!/usr/bin/env python3
import os
import requests

# List of dictionaries
post = []

# Create the list of dictionaries from the text files
for tf in os.listdir(path='./supplier-data/descriptions/'):
  with open(file='/home/student-00-e70fad3680b2/supplier-data/descriptions/' + tf, mode='r') as f:
    data = f.readlines()
    name, weight, description = data[0].strip(), int(data[1].split()[0]), ' '.join([line.strip() for line in data[2:]])
    post.append(
      {
        'name': name,
        'weight': weight,
        'description': description,
        'image_name': tf.split('.')[0] + '.jpeg'
      }
    )

# Send POST requests to API endpoint
for payload in post:
  r = requests.post(url='http://35.192.15.30/fruits/', data=payload)
  r.raise_for_status()