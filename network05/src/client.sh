#!/bin/sh

python3 /client.py --ca-certs /ca_cert.pem -k --secrets-log /logs/secrets-log https://server:4433/
echo "sleeping..."
sleep 10