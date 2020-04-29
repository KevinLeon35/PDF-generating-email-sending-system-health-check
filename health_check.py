!# /usr/bin/env python3

import shutil
import psutil
import socket
import emails

def check_disk_usage(disk):

  du = shutil.disk_usage(disk)
  free = du.free / du.total * 100
  return free > 20

def check_cpu_usage():
  usage = psutil.cpu.percent(1)
  return usage < 80

def check_network_localhost():
  localhost = socket.gethostbyname('localhost')
  return localhost == '127.0.0.1'

def check_memory_usage(memory):
  mem = psutil.virtual_memory(memory)
  return mem.available < 500

def main():
  while True:
    if not check_disk_usage('/'):
      email = emails.generate_email("automation@example.com", "username@example.com", "Error - Available disk space is less than 20%", "Please check your system and resolve the issue as soon as possible")
      emails.send_email(email)
    if not check_cpu_usage():
      email = emails.generate_email("automation@example.com", "username@example.com", "Error - CPU usage is over 80%", "Please check your system and resolve the issue as soon as possible")
      emails.send_email(email)
    if not check_network_localhost():
      email = emails.generate_email("automation@example.com", "username@example.com", "Error - localhost cannot be resolved to 127.0.0.1", "Please check your system and resolve the issue as soon as possible")
      emails.send_email(email)
    if check_memory_usage('/'):
      email = emails.generate_email("automation@example.com", "username@example.com", "Error - Available memory is less than 500MB", "Please check your system and resolve the issue as soon as possible")
      emails.send_email(email)
    time.sleep(60)

if __name__ == "__main__":
  main()
