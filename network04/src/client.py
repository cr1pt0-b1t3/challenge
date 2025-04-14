import sys
import time
import requests

def main(addr: tuple[str, int]):

    url = f"http://{addr[0]}:{addr[1]}"
    session = requests.Session()

    print(session.get(f'{url}/step1').text)

    params = {'hello': 'world', 'dead': 'beef'}
    print(session.post(f'{url}/step2', data=params).text)

    print(session.put(f'{url}/step3').text)
    print(session.delete(f'{url}/step4').text)

    time.sleep(3)

if __name__ == '__main__':
    time.sleep(3)
    main((sys.argv[1], int(sys.argv[2])))
