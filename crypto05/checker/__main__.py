#!/usr/bin/python3

import logging
import os

import requests

logging.disable()

URL = os.environ.get("URL", "http://passwordlesslogin.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]

r = requests.post(f'{URL}/execute', json={'fn': 'register', 'inputs': ['Amministratori']})
r.raise_for_status()
r1 = r.json()['result']

r = requests.post(f'{URL}/execute', json={'fn': 'register', 'inputs': ['Bmministratore']})
r.raise_for_status()
r2 = r.json()['result']

r = requests.post(f'{URL}/execute', json={'fn': 'login', 'inputs': [r1[:32] + r2[32:]]})
r.raise_for_status()
print(r.json()['result'])
