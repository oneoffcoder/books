import socket
import threading
import time
from stats import Stats

class Tello(object):
    def __init__(self):
        """
        Constructor.
        """
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

        # thread for receiving cmd ack
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_address = (self.tello_ip, self.tello_port)
        self.log = []

        self.MAX_TIME_OUT = 15.0

    def send_command(self, command):
        """
        Send a command to the ip address. Will be blocked until
        the last command receives an 'OK'.
        If the command fails (either b/c time out or error),
        will try to resend the command
        :param command: (str) the command to send
        :param ip: (str) the ip of Tello
        :return: The latest command response
        """
        self.log.append(Stats(command, len(self.log)))

        self.socket.sendto(command.encode('utf-8'), self.tello_address)
        print(f'sending command: {command} to {self.tello_ip}')

        start = time.time()
        while not self.log[-1].got_response():
            now = time.time()
            diff = now - start
            if diff > self.MAX_TIME_OUT:
                print(f'Max timeout exceeded... command {command}')
                return
        print(f'Done!!! sent command: {command} to {self.tello_ip}')

    def _receive_thread(self):
        """
        Listen to responses from the Tello.
        Runs as a thread, sets self.response to whatever the Tello last returned.
        """
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print(f'from {ip}: {self.response}')

                self.log[-1].add_response(self.response)
            except Exception as exc:
                print(f'Caught exception socket.error : {exc}')

    def on_close(self):
        """
        On close.
        :returns: None.
        """
        pass

    def get_log(self):
        """
        Gets the logs.
        :returns: Logs.
        """
        return self.log