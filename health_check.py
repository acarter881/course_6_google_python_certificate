#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails

# Check if CPU usage is over 80%
def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return usage <= 80

# Check if available disk space is less than 20%
def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free / du.total * 100
  return free >= 20

# Check if available memory is less than 500MB
def avail_memory():
  mem = psutil.virtual_memory()
  THRESHOLD = 500 * 1024 * 1024 # 500MB
  return mem.available >= THRESHOLD

# Check if localhost can't resolve to 127.0.0.1
def check_localhost():
  return socket.getaddrinfo("localhost","http")[0][4][0] == '::1'

if __name__ == '__main__':
  if not check_cpu_usage():
    subject = 'Error - CPU usage is over 80%'
  if not check_disk_usage('/'):
    subject = 'Error - Available disk space is less than 20%'
  if not avail_memory():
    subject = 'Error - Available memory is less than 500MB'
  if not check_localhost():
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'

  # If one of the checks returns False
  if not check_cpu_usage() or not check_disk_usage('/') or not avail_memory() or not check_localhost():
    message = emails.generate_error_report(
    sender='automation@example.com',
    recipient='student-00-e70fad3680b2@example.com',
    subject=subject,
    body='Please check your system and resolve the issue as soon as possible.')
    emails.send_email(message=message)
