#!/usr/bin/python3

import logging
import os

import requests

logging.disable()

URL = os.environ.get("URL", "http://secretcheckai.challs.olicyber.it")
if URL.endswith("/"):
    URL = URL[:-1]

r = requests.get(URL)
r.raise_for_status()

assert 'aXQwNG5kXzExbHM0X3ZuXzMzdmQzMXJzX190dGhuMzNfMXNsMGNse3VDdEUxUzBBblQhSX0=' in r.text

print('ITASEC{cl13nt_s1d3_v4l1d4ti0n_1s_n3v3r_th3_s0lut10n!}')
