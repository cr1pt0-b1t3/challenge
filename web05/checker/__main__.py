#!/usr/bin/python3

import logging
import os

import requests

logging.disable()

URL = os.environ.get("URL", "http://dividifacile.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]

r = requests.post(f'{URL}/divide', json={'amount': '69', 'pieces': '0'})
r.raise_for_status()

print(r.text)
