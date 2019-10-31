import socket
import sys
import time

HOST, PORT = 'localhost', 301
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    print('socket opened')

    while True:    
        received = str(sock.recv(1024), 'utf-8')
        if len(received.strip()) > 0:
            print(f'{received}')
        time.sleep(1)
finally:
    sock.close()
    print('socket closed')