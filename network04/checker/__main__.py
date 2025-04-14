#!/usr/bin/python3

import os
import requests
import logging
logging.disable()

URL = os.environ.get("URL", "http://lemosse.challs.olicyber.it")
if URL.endswith("/"):
   URL = URL[:-1]

session = requests.Session()
session.get(f'{URL}/step1')
params = {'hello': 'world', 'dead': 'beef'}
session.post(f'{URL}/step2', data=params)
session.put(f'{URL}/step3')
print(session.delete(f'{URL}/step4').text)
