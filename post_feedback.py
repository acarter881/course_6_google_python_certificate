#!/usr/bin/env python3
import os
import requests

# List of dictionaries
post = []

# Create the list of dictionaries from the text files
for file in os.listdir(path='/data/feedback/'):
  with open(file='/data/feedback/' + file, mode='r') as f:
    data = f.readlines()
    title, name, date, feedback = data[0].strip(), data[1].strip(), data[2].strip(), ' '.join([line.strip() for line in data[3:]])
    post.append(
      {
        'title': title,
        'name': name,
        'date': date,
        'feedback': feedback
      }
    )

# Send POST requests to API endpoint
for payload in post:
  r = requests.post(url='http://35.239.216.174/feedback/', data=payload)
  r.raise_for_status()
