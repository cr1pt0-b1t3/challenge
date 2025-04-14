#!/usr/bin/python3

import logging
import os

import requests

logging.disable()

URL = os.environ.get("URL", "http://xorminimale.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]

r = requests.post(f'{URL}/execute', json={'fn': 'get_encrypted_flag', 'inputs': []})
r.raise_for_status()

r = bytes.fromhex(r.json()['result'])
c = r[0] ^ ord('I')
print(''.join([chr((c + i) ^ cc) for i, cc in enumerate(r)]))
