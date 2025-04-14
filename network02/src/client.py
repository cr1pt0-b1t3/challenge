import sys
import time
from socket import socket
from typing import Optional

def main(addr: tuple[str, int]):
    s = socket()
    s.connect(addr)

    fd = open("/dev/urandom", "rb")

    for i in range(300):
        if i % 70 == 0:
            s.send(fd.read(300))
        else:
            s.send(fd.read(5))
        time.sleep(0.2)

    print('Sent all bytes')        

    fd.close()
    time.sleep(3)
    s.close()


if __name__ == '__main__':
    time.sleep(3)
    main((sys.argv[1], int(sys.argv[2])))
