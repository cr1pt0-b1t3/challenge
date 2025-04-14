import sys
import time
import requests

def main(addr: tuple[str, int], filename: str):

    url = f"http://{addr[0]}:{addr[1]}"
    
    print("Visiting server")
    requests.get(url)

    print("Uploading wrong stuff" )
    files = { 'file': b"blablablabla" }
    res = requests.post(f"{url}/upload", files=files)
    print(res.text)

    print("Uploading wrong stuff" )
    files = { 'file': b"bleblebleble" }
    res = requests.post(f"{url}/upload", files=files)
    print(res.text)

    print("Uploading file")
    files = { 'file': open(filename, 'rb') }
    res = requests.post(f"{url}/upload", files=files)
    print(res.text)

    print("Uploading wrong stuff" )
    files = { 'file': b"blibliblibli" }
    res = requests.post(f"{url}/upload", files=files)
    print(res.text)
    time.sleep(2)


if __name__ == '__main__':
    time.sleep(2)
    main((sys.argv[1], int(sys.argv[2])), sys.argv[3])
