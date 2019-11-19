import socket
import threading
import time

class Tello(object):
    """
    Wrapper class to interact with the Tello drone.
    """

    def __init__(self, local_ip, local_port, imperial=False, 
                 command_timeout=.3, 
                 tello_ip='192.168.10.1',
                 tello_port=8889):
        """
        Binds to the local IP/port and puts the Tello into command mode.

        :param local_ip: Local IP address to bind.
        :param local_port: Local port to bind.
        :param imperial: If True, speed is MPH and distance is feet. If False, speed is KPH and distance is meters.
        :param command_timeout: Number of seconds to wait for a response to a command.
        :param tello_ip: Tello IP.
        :param tello_port: Tello port.
        """
        self.abort_flag = False
        self.command_timeout = command_timeout
        self.imperial = imperial
        self.response = None  
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
        self.tello_address = (tello_ip, tello_port)
        self.last_height = 0
        self.socket.bind((local_ip, local_port))

        # thread for receiving cmd ack
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.socket.sendto(b'command', self.tello_address)
        print ('sent: command')

    def __del__(self):
        """
        Closes the local socket.

        :return: None.
        """
        self.socket.close()

    def _receive_thread(self):
        """
        Listen to responses from the Tello.

        Runs as a thread, sets self.response to whatever the Tello last returned.

        :return: None.
        """
        while True:
            try:
                self.response, ip = self.socket.recvfrom(3000)
            except socket.error as exc:
                print(f'Caught exception socket.error : {exc}')

    def send_command(self, command):
        """
        Send a command to the Tello and wait for a response.

        :param command: Command to send.
        :return: Response from Tello.
        """
        print(f'>> send cmd: {command}')
        self.abort_flag = False
        timer = threading.Timer(self.command_timeout, self.set_abort_flag)

        self.socket.sendto(command.encode('utf-8'), self.tello_address)

        timer.start()
        while self.response is None:
            if self.abort_flag is True:
                break
        timer.cancel()
        
        if self.response is None:
            response = 'none_response'
        else:
            response = self.response.decode('utf-8')

        self.response = None

        return response
    
    def set_abort_flag(self):
        """
        Sets self.abort_flag to True.

        Used by the timer in Tello.send_command() to indicate to that a response        
        timeout has occurred.

        :return: None.
        """
        self.abort_flag = True

    def takeoff(self):
        """
        Initiates take-off.

        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.send_command('takeoff')

    def set_speed(self, speed):
        """
        Sets speed.

        This method expects KPH or MPH. The Tello API expects speeds from
        1 to 100 centimeters/second.

        Metric: .1 to 3.6 KPH
        Imperial: .1 to 2.2 MPH

        :param speed: Speed.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        speed = float(speed)

        if self.imperial is True:
            speed = int(round(speed * 44.704))
        else:
            speed = int(round(speed * 27.7778))

        return self.send_command('speed %s' % speed)

    def rotate_cw(self, degrees):
        """
        Rotates clockwise.

        :param degrees: Degrees to rotate, 1 to 360.
        :return:Response from Tello, 'OK' or 'FALSE'.
        """
        return self.send_command('cw %s' % degrees)

    def rotate_ccw(self, degrees):
        """
        Rotates counter-clockwise.

        :param degrees: Degrees to rotate, 1 to 360.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.send_command('ccw %s' % degrees)

    def flip(self, direction):
        """
        Flips.

        :param direction: Direction to flip, 'l', 'r', 'f', 'b'.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.send_command('flip %s' % direction)

    def get_response(self):
        """
        Returns response of tello.

        :return: Response of tello.
        """
        response = self.response
        return response

    def get_height(self):
        """
        Returns height(dm) of tello.

        :return: Height(dm) of tello.
        """
        height = self.send_command('height?')
        height = str(height)
        height = filter(str.isdigit, height)
        try:
            height = int(height)
            self.last_height = height
        except:
            height = self.last_height
            pass
        return height

    def get_battery(self):
        """
        Returns percent battery life remaining.

        :return: Percent battery life remaining.
        """
        battery = self.send_command('battery?')

        try:
            battery = int(battery)
        except:
            pass

        return battery

    def get_flight_time(self):
        """
        Returns the number of seconds elapsed during flight.

        :return: Seconds elapsed during flight.
        """
        flight_time = self.send_command('time?')

        try:
            flight_time = int(flight_time)
        except:
            pass

        return flight_time

    def get_speed(self):
        """
        Returns the current speed.

        :return: Current speed in KPH or MPH.
        """
        speed = self.send_command('speed?')

        try:
            speed = float(speed)

            if self.imperial is True:
                speed = round((speed / 44.704), 1)
            else:
                speed = round((speed / 27.7778), 1)
        except:
            pass

        return speed

    def land(self):
        """
        Initiates landing.

        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.send_command('land')

    def move(self, direction, distance):
        """
        Moves in a direction for a distance.

        This method expects meters or feet. The Tello API expects distances
        from 20 to 500 centimeters.

        Metric: .02 to 5 meters
        Imperial: .7 to 16.4 feet

        :param direction: Direction to move, 'forward', 'back', 'right' or 'left'.
        :param distance: Distance to move.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        distance = float(distance)

        if self.imperial is True:
            distance = int(round(distance * 30.48))
        else:
            distance = int(round(distance * 100))

        return self.send_command('%s %s' % (direction, distance))

    def move_backward(self, distance):
        """
        Moves backward for a distance.

        See comments for Tello.move().

        :param distance: Distance to move.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.move('back', distance)

    def move_down(self, distance):
        """
        Moves down for a distance.

        See comments for Tello.move().

        :param distance: Distance to move.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.move('down', distance)

    def move_forward(self, distance):
        """
        Moves forward for a distance.

        See comments for Tello.move().

        :param distance: Distance to move.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.move('forward', distance)

    def move_left(self, distance):
        """
        Moves left for a distance.

        See comments for Tello.move().

        :param distance: Distance to move.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.move('left', distance)

    def move_right(self, distance):
        """
        Moves right for a distance.

        See comments for Tello.move().

        :param distance: Distance to move.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.move('right', distance)

    def move_up(self, distance):
        """
        Moves up for a distance.

        See comments for Tello.move().

        :param distance: Distance to move.
        :return: Response from Tello, 'OK' or 'FALSE'.
        """
        return self.move('up', distance)
