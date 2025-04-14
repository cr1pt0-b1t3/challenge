#!/usr/bin/python3

import logging
import os

import requests

logging.disable()

URL = os.environ.get("URL", "http://condividendosegreti.challs.olicyber.it")
if URL.endswith("/"):
   URL = URL[:-1]

r = requests.post(f'{URL}/execute', json={'fn': 'get_flag_shares', 'inputs': []})
r.raise_for_status()
shares = r.json()['result']
shares += [792797163472027]

r = requests.post(f'{URL}/execute', json={'fn': 'recover_secret', 'inputs': [','.join(str(x) for x in shares)]})
r.raise_for_status()

print(r.json()['result'])
