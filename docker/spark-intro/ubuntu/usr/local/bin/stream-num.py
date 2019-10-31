import socketserver
import time
from random import randint

class NumberTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('NumberTCPHandler')

        try:
            while True:
                s = f'{randint(1, 100)}'
                b = bytes(s, 'utf-8')
                self.request.sendall(b)
                time.sleep(1)
        except BrokenPipeError:
            print('broken pipe detected')

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 300

    server = socketserver.TCPServer((host, port), NumberTCPHandler)
    print(f'server starting {host}:{port}')
    server.serve_forever()
        