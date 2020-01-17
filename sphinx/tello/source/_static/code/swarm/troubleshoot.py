import socket
import argparse
import sys
import time

def get_socket():
    """
    Gets a socket.
    :return: Socket.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 8889))

    return s

def send_commands(commands, address):
    """
    Sends a list of commands to the Tello.
    """
    socket = get_socket()

    for command in commands:
        command = command.encode('utf-8')
        print(f'[SEND] {address[0]}: {command.decode("utf-8")}')
        socket.sendto(command, address)

        response, ip = socket.recvfrom(1024)
        response = response.decode('utf-8')
        print(f'[RECEIVE] {ip[0]}: {response}')

        time.sleep(1)

if __name__ == '__main__':
    commands = [
        'command',
        'speed?',
        'battery?',
        'time?',
        'wifi?',
        'sdk?',
        'sn?',
        'streamon',
        'mon',
        'mdirection 2'
    ]

    address = ('192.168.10.1', 8889)

    send_commands(commands, address)