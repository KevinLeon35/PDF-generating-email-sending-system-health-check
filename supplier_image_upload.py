#! /usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
for images in os.listdir('/home/student-04-f312d8e8e665/supplier-data/images'):
  if "jpeg" in images:
    with open('/home/student-04-f312d8e8e665/supplier-data/images/' + images, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
