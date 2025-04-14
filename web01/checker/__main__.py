#!/usr/bin/python3

import logging
import os
import re

import requests

logging.disable()

URL = os.environ.get("URL", "http://vectorcraft.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]

r = requests.get(f'{URL}/logo.svg')
r.raise_for_status()

print(re.search(r'ITASEC\{.+?}', r.text).group())
