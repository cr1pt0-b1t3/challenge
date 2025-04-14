#!/usr/bin/python3

import logging
import os

import requests

logging.disable()

URL = os.environ.get("URL", "http://sitogentile.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]

r = requests.get(f'{URL}/talk')
r.raise_for_status()

flag = {}
for h in r.headers:
    if not h.startswith('X-Flag-'):
        continue

    flag[int(h[7:])] = r.headers[h]

print(''.join([flag[i] for i in range(max(flag.keys())+1)]))
