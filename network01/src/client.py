import sys
import time
from socket import socket
from typing import Optional

FLAG = b"ITASEC{l3ts_f0llow_th3_flow_and_the_fl4g_will_sh0w_up}"

def recv_all(sock: socket, n: int) -> Optional[bytes]:
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data


def main(addr: tuple[str, int]):
    s = socket()
    s.connect(addr)

    msg = recv_all(s, 0x12)

    for char in FLAG:
        s.send(bytes([char]))
        time.sleep(0.2)

    print('Sent flag')        

    time.sleep(5)
    s.close()


if __name__ == '__main__':
    time.sleep(5)
    main((sys.argv[1], int(sys.argv[2])))
