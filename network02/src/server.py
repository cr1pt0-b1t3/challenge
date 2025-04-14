import sys
import time
from socket import socket, SOL_SOCKET, SO_REUSEADDR
from typing import Optional

def main(port: int):
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', port))
    s.listen()

    while True:
        ss, addr = s.accept()
        print('New client', addr)

        ss.send(b"Give me the flag!\n")

        msg = b""
        for i in range(300):
            if i % 70 == 0:
                ss.recv(300)
            else:
                ss.recv(5)
            time.sleep(0.2)

        ss.close()
        print('Disconnected client', addr)


if __name__ == '__main__':
    main(int(sys.argv[1]))
