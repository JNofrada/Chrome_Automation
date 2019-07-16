
import chrome_bookmarks
import webbrowser
import sys
import time
import pytest
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:


def main():
    for url in chrome_bookmarks.urls:
        print(url.name)
        time.sleep(1)
        if (url.url == 'https://valiantny.sharepoint.com/sites/CMChangeManagement' or url.url == 'https://developers.google.com/api-client-library/python/'):
            continue
        webbrowser.open(url.url)
    sys.exit("0")

if __name__ == '__main()__':
    main()