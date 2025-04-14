import sys
from socket import socket, SOL_SOCKET, SO_REUSEADDR
from typing import Optional

def recv_all(sock: socket, n: int) -> Optional[bytes]:
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

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
        while True:
            char = ss.recv(1)
            msg += char
            if char == b"}":
                break

        print(f'Received {msg}')

        ss.close()
        print('Disconnected client', addr)


if __name__ == '__main__':
    main(int(sys.argv[1]))
