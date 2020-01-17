import threading
from threading import Thread
import socket
import time
import netifaces
import netaddr
from netaddr import IPNetwork
from collections import defaultdict
import binascii
from datetime import datetime
import itertools

class Tello(object):
    """
    A wrapper class to interact with Tello.
    Communication with Tello is handled by TelloManager.
    """
    def __init__(self, tello_ip, tello_manager):
        """
        Ctor.
        :param tello_ip: Tello IP.
        :param tello_manager: Tello Manager.
        """
        self.tello_ip = tello_ip
        self.tello_manager = tello_manager

    def send_command(self, command):
        """
        Sends a command.
        :param command: Command.
        :return: None.
        """
        return self.tello_manager.send_command(command, self.tello_ip)

    def __repr__(self):
        return f'TELLO@{self.tello_ip}'


class TelloManager(object):
    """
    Tello Manager.
    """

    def __init__(self):
        """
        Ctor.
        """
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

        # thread for receiving cmd ack
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.tello_ip_list = []
        self.tello_list = []
        self.log = defaultdict(list)

        self.COMMAND_TIME_OUT = 20.0

        self.last_response_index = {}
        self.str_cmd_index = {}

    def find_avaliable_tello(self, num):
        """
        Find Tellos.
        :param num: Number of Tellos to search.
        :return: None
        """
        possible_ips = self.get_possible_ips()

        print(f'[SEARCHING], Searching for {num} from {len(possible_ips)} possible IP addresses')

        iters = 0

        while len(self.tello_ip_list) < num:
            print(f'[SEARCHING], Trying to find Tellos, number of tries = {iters + 1}')

            # delete already found Tello
            for tello_ip in self.tello_ip_list:
                if tello_ip in possible_ips:
                    possible_ips.remove(tello_ip)

            # skip server itself
            for ip in possible_ips:
                cmd_id = len(self.log[ip])
                self.log[ip].append(Stats('command', cmd_id))

                # print(f'{iters}: sending command to {ip}:8889')

                try:
                    self.socket.sendto(b'command', (ip, 8889))
                except:
                    print(f'{iters}: ERROR: {ip}:8889')
                    pass

            iters = iters + 1
            time.sleep(5)

        # filter out non-tello addresses in log
        temp = defaultdict(list)
        for ip in self.tello_ip_list:
            temp[ip] = self.log[ip]
        self.log = temp

    def get_possible_ips(self):
        """
        Gets all the possible IP addresses for subnets that the computer is a part of.
        :return: List of IP addresses.
        """
        infos = self.get_subnets()
        ips = SubnetInfo.flatten([info.get_ips() for info in infos])
        ips = list(filter(lambda ip: ip.startswith('192.168.3.'), ips))
        return ips

    def get_subnets(self):
        """
        Gets all subnet information.

        :return: List of subnet information.
        """
        infos = []

        for iface in netifaces.interfaces():
            addrs = netifaces.ifaddresses(iface)

            if socket.AF_INET not in addrs:
                continue

            # Get ipv4 stuff
            ipinfo = addrs[socket.AF_INET][0]
            address, netmask = ipinfo['addr'], ipinfo['netmask']

            # limit range of search. This will work for router subnets
            if netmask != '255.255.255.0':
                continue

            # Create ip object and get
            cidr = netaddr.IPNetwork(f'{address}/{netmask}')
            network = cidr.network

            info = SubnetInfo(address, network, netmask)
            infos.append(info)

        return infos

    def get_tello_list(self):
        return self.tello_list

    def send_command(self, command, ip):
        """
        Sends a command to the IP address. Will be blocked until the last command receives an 'OK'.
        If the command fails (either b/c time out or error),  will try to resend the command.

        :param command: Command.
        :param ip: Tello IP.
        :return: Response.
        """
        #global cmd
        command_sof_1 = ord(command[0])
        command_sof_2 = ord(command[1])

        if command_sof_1 == 0x52 and command_sof_2 == 0x65:
            multi_cmd_send_flag = True
        else :
            multi_cmd_send_flag = False

        if multi_cmd_send_flag == True:      
            self.str_cmd_index[ip] = self.str_cmd_index[ip] + 1
            for num in range(1,5):                
                str_cmd_index_h = self.str_cmd_index[ip] / 128 + 1
                str_cmd_index_l = self.str_cmd_index[ip] % 128
                if str_cmd_index_l == 0:
                    str_cmd_index_l = str_cmd_index_l + 2
                cmd_sof = [0x52, 0x65, str_cmd_index_h, str_cmd_index_l, 0x01, num + 1, 0x20]
                cmd_sof_str = str(bytearray(cmd_sof))
                cmd = cmd_sof_str + command[3:]
                self.socket.sendto(cmd.encode('utf-8'), (ip, 8889))

            print(f'[MULTI_COMMAND], IP={ip}, COMMAND={command[3:]}')
            real_command = command[3:]
        else:
            self.socket.sendto(command.encode('utf-8'), (ip, 8889))
            print(f'[SINGLE_COMMAND] IP={ip}, COMMAND={command}')
            real_command = command
        
        self.log[ip].append(Stats(real_command, len(self.log[ip])))
        start = time.time()

        while not self.log[ip][-1].got_response():
            now = time.time()
            diff = now - start
            if diff > self.COMMAND_TIME_OUT:
                print(f'[NO_RESPONSE] Max timeout exceeded for command: {real_command}')
                return    

    def _receive_thread(self):
        """
        Listen to responses from the Tello.
        Runs as a thread, sets self.response to whatever the Tello last returned.

        :return: None.
        """
        while True:
            try:
                response, ip = self.socket.recvfrom(1024)
                response = response.decode('utf-8')
                self.response = response
                
                ip = ''.join(str(ip[0]))                
                
                if self.response.upper() == 'OK' and ip not in self.tello_ip_list:
                    self.tello_ip_list.append(ip)
                    self.last_response_index[ip] = 100
                    self.tello_list.append(Tello(ip, self))
                    self.str_cmd_index[ip] = 1
                
                response_sof_part1 = ord(self.response[0])               
                response_sof_part2 = ord(self.response[1])

                if response_sof_part1 == 0x52 and response_sof_part2 == 0x65:
                    response_index = ord(self.response[3])
                    
                    if response_index != self.last_response_index[ip]:
                        print(f'[MULTI_RESPONSE], IP={ip}, RESPONSE={self.response[7:]}')
                        self.log[ip][-1].add_response(self.response[7:], ip)
                    self.last_response_index[ip] = response_index
                else:
                    # print(f'[SINGLE_RESPONSE], IP={ip}, RESPONSE={self.response}')
                    self.log[ip][-1].add_response(self.response, ip)
                         
            except socket.error as exc:
                # swallow exception
                # print "[Exception_Error]Caught exception socket.error : %s\n" % exc
                pass

    def get_log(self):
        """
        Get all logs.
        :return: Dictionary of logs.
        """
        return self.log

    def get_last_logs(self):
        """
        Gets the last logs.
        :return: List of last logs.
        """
        return [log[-1] for log in self.log.values()]


class SubnetInfo(object):
    """
    Subnet information.
    """

    def __init__(self, ip, network, netmask):
        """
        Ctor.
        :param ip: IP.
        :param network: Network.
        :param netmask: Netmask.
        """
        self.ip = ip
        self.network = network
        self.netmask = netmask

    def __repr__(self):
        return f'{self.network} | {self.netmask} | {self.ip}'

    def get_ips(self):
        """
        Gets all the possible IP addresses in the subnet.
        :return: List of IPs.
        """
        def get_quad(ip):
            """
            Gets the third quad.
            :param ip: IP.
            :return: Third quad.
            """
            quads = str(ip).split('.')
            quad = quads[3]
            return quad
        
        def is_valid(ip):
            """
            Checks if IP is valid.
            :return: A boolean indicating if IP is valid.
            """
            quad = get_quad(ip)
            result = False if quad == '0' or quad == '255' else True

            if result:
                if str(ip) == self.ip:
                    result = False
            
            return result

        ip_network = IPNetwork(f'{self.network}/{self.netmask}')

        return [str(ip) for ip in ip_network if is_valid(ip)]

    @staticmethod
    def flatten(infos):
        return list(itertools.chain.from_iterable(infos))


class Stats(object):
    """
    Statistics
    """

    def __init__(self, command, id):
        """
        Ctor.
        :param command: Command.
        :param id: ID.
        """
        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None
        self.drone_ip = None

    def add_response(self, response, ip):
        """
        Adds a response.
        :param response: Response.
        :param ip: IP address.
        :return: None.
        """
        if self.response == None:
            self.response = response
            self.end_time = datetime.now()
            self.duration = self.get_duration()
            self.drone_ip = ip

    def get_duration(self):
        """
        Gets the duration.
        :return: Duration (seconds).
        """
        diff = self.end_time - self.start_time
        return diff.total_seconds()

    def print_stats(self):
        """
        Prints statistics.
        :return: None.
        """
        print(self.get_stats())

    def got_response(self):
        """
        Checks if response was received.
        :return: A boolean indicating if response was received.
        """
        return False if self.response is None else True

    def get_stats(self):
        """
        Gets the statistics.
        :return: Statistics.
        """
        return {
            'id': self.id,
            'command': self.command,
            'response': self.response,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'duration': self.duration
        }

    def get_stats_delimited(self):
        stats = self.get_stats()
        keys = ['id', 'command', 'response', 'start_time', 'end_time', 'duration']
        vals = [f'{k}={stats[k]}' for k in keys]
        vals = ', '.join(vals)
        return vals

    def __repr__(self):
        return self.get_stats_delimited()