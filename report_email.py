#!/usr/bin/env python3
import os
from datetime import date
import reports
import emails

# Get today's date (i.e., October 04, 2021)
today = date.today()
d1 = today.strftime('%B %d, %Y')
report_title = 'Processed Update on ' + d1

# List of data for PDF file
pdf_list = []

# Iterate over text files and append relevant data to list
for thing in os.listdir('./supplier-data/descriptions'):
  file = '/home/student-00-e70fad3680b2/supplier-data/descriptions/' + thing
  with open (file=file, mode='r') as tf:
    data = tf.readlines()
    name = 'name: ' + data[0].strip()
    weight = 'weight: ' + data[1].strip()
    pdf_list.extend((name, weight, '\n'))

# Format the paragraph for the PDF file
paragraph = ' '.join([line + '<br/>' for line in pdf_list])

# Generate PDF file, create email, send email
if __name__ == '__main__':
  reports.generate_report(attachment='/tmp/processed.pdf', title=report_title, paragraph=paragraph)
  message = emails.generate_email(
    sender='automation@example.com',
    recipient='student-00-e70fad3680b2@example.com',
    subject='Upload Completed - Online Fruit Store',
    body='All fruits are uploaded to our website successfully. A detailed list is attached to this email.',
    attachment_path='/tmp/processed.pdf')
  emails.send_email(message=message)