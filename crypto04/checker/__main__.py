#!/usr/bin/python3

import logging
import os

import requests

logging.disable()

URL = os.environ.get("URL", "http://xortemporale.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]

r = requests.post(f'{URL}/execute', json={'fn': 'get_encrypted_flag', 'inputs': []})
r.raise_for_status()

r = requests.post(f'{URL}/execute', json={'fn': 'temporal_xor', 'inputs': [r.json()['result']]})
r.raise_for_status()

print(bytes.fromhex(r.json()['result']).decode())
