import socketserver
import time
from random import choice

class AlphaTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('AlphaTCPHandler')
        alphabets = list('abcdefghikjklmnopqrstuvwxyz')

        try:
            while True:
                s = f'{choice(alphabets)}'
                b = bytes(s, 'utf-8')
                self.request.sendall(b)
                time.sleep(1)
        except BrokenPipeError:
            print('broken pipe detected')

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 301

    server = socketserver.TCPServer((host, port), AlphaTCPHandler)
    print(f'server starting {host}:{port}')
    server.serve_forever()
        