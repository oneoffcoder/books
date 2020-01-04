from collections import namedtuple
import socket
import threading
from threading import Thread
import queue
from datetime import datetime
import time
import traceback

Address = namedtuple('Address', 'ip, port')

class AtomicInt(object):
    def __init__(self, initial=0):
        self.value = initial
        self._lock = threading.Lock()

    def increment(self, num=1):
        with self._lock:
            self.value += num
            return self.value

class LogItem(object):
    """
    Log item.
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
            self.duration = self._get_duration()
            self.drone_ip = ip

    def _get_duration(self):
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

class Swarm(object):

    def __init__(self, local_address, drones, commands):
        self.n_drones_ready = AtomicInt()
        self.local_address = local_address
        self.drones = drones
        self.commands = commands

    def _get_local_address(self):
        return (self.local_address.ip, self.local_address.port)

    def init(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self._get_local_address())

        for drone in self.drones:
            drone.init(self.socket, self)

        n_drones = len(self.drones)
        while True:
            if self.n_drones_ready.value != n_drones:
                time.sleep(0.5)
            else:
                print(f'SWARM | {n_drones} initialized')
                break
    
    def deinit(self):
        try:
            self.socket.close()
            print(f'SWARM DEINIT | socket_close | success')
        except Exception as e:
            print(f'SWARM DEINIT | socket_close | {e}')
        
        for drone in self.drones:
            drone.deinit()

    def start(self):
        for command in self.commands:
            if '>' in command:
                self._handle_command(command)
            elif 'sync' in command:
                self._handle_sync(command)
    
    def _handle_command(self, command):
        for drone in self.drones:
            drone.add_command(command)

    def _handle_sync(self, command):
        def get_time_out(command):
            tokens = [t.strip() for t in command.partition('sync')]
            tokens = [t for t in tokens if len(t) > 0]
            return float(tokens[1])
            
        TIME_OUT = get_time_out(command)

        self._sync(TIME_OUT)

    def wait(self):
        self._sync()

    def _sync(self, TIME_OUT=None):
        def get_queues():
            return [d.queue for d in self.drones]
        
        def all_queues_empty():
            queues = [q for q in get_queues() if not q.empty()]
            return False if len(queues) > 0 else True

        def get_last_logs():
            return [d.logs[-1] for d in self.drones]

        def all_responses_received():
            logs = [log for log in get_last_logs() if not log.got_response()]
            return False if len(logs) > 0 else True

        start = time.time()

        while not all_queues_empty():
            if TIME_OUT is not None:
                now = time.time()
                diff = now - start

                if diff > TIME_OUT:
                    print(f'SYNC | FAILED | queues_not_empty | waited {diff:.1f} | exceeded {TIME_OUT}')
                    break
            else:
                time.sleep(0.5)
        
        while not all_responses_received():
            if TIME_OUT is not None:
                now = time.time()
                diff = now - start

                if diff > TIME_OUT:
                    print(f'SYNC | FAILED | responses_not_received | waited {diff:.1f} | exceeded {TIME_OUT}')
                    break
            else:
                time.sleep(0.5)
    
    def finished_initializing(self, drone):
        self.n_drones_ready.increment()
    
class Drone(object):
    def __init__(self, tid, drone_address):
        self.tid = tid
        self.drone_address = drone_address

        self.queue = queue.Queue()
        
        self.logs = []
        self.active = False
        self.n_commands = 0
        self.n_responses = 0

    def _get_drone_address(self):
        return (self.drone_address.ip, self.drone_address.port)

    def init(self, socket, listener=None):
        self.socket = socket
        self.stop_thread = False

        self.receive_thread = Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.send_thread = Thread(target=self._send_thread)
        self.send_thread.daemon = True
        self.send_thread.start()

        if listener is not None:
            listener.finished_initializing(self)

    def deinit(self):
        self.stop_thread = True

        try:
            self.receive_thread.join()
            print(f'DEINIT | {self.__repr__()} | receive_thread | join success')
        except Exception as e:
            print(f'DEINIT | {self.__repr__()} | receive_thread | {e}')
        
        try:
            self.send_thread.join()
            print(f'DEINIT | {self.__repr__()} | send_thread | join success')
        except Exception as e:
            print(f'DEINIT | {self.__repr__()} | send_thread | {e}')

    def add_command(self, command):
        """
        Queues up a command to send.

        :param command: Command.
        """
        tokens = [t.strip() for t in command.partition('>')]
        tid, action = tokens[0], tokens[2]

        if tid == '*' or tid == str(self.tid):
            print(f'ACTION | {self.__repr__()} | queued | {action}')
            self.queue.put(action)

    def __repr__(self):
        return f'TELLO@{self.drone_address.ip}:{self.drone_address.port}'

    def _wait_for_response(self):
        COMMAND_TIME_OUT = 10.0

        start = time.time()

        while not self.logs[-1].got_response():
            now = time.time()
            diff = now - start

            if diff > COMMAND_TIME_OUT:
                print(f'WAIT RESPONSE | {self.__repr__()} | timeout | {diff} | {self.logs[-1].command} | {self.logs[-1].got_response()}')
                break
            else:
                # print(f'WAIT RESPONSE | {self.__repr__()} | waiting | {diff} | {self.logs[-1].command} | {self.logs[-1].got_response()}')
                pass
        # print(f'WAIT RESPONSE | {self.__repr__()} | finished_waiting | {diff} | {self.logs[-1].command} | {self.logs[-1].got_response()}')

    def _send_thread(self):
        """
        Sends commands to the drone.

        :return: None.
        """
        while True:
            if self.stop_thread:
                print('THREAD | SEND | stopping')
                break

            if self.queue.empty():
                continue

            if self.n_responses < self.n_commands:
                continue
            
            try:
                command = self.queue.get()
                
                self.socket.sendto(command.encode('utf-8'), self._get_drone_address())
                print(f'COMMAND | {self.__repr__()} | {command}')
                
                self.n_commands = self.n_commands + 1
                
                log_item = LogItem(command, self.n_commands)
                self.logs.append(log_item)

                self._wait_for_response()
            except socket.error as e:
                print(f'THREAD | SEND | socket_error | {e}')
            finally:
                # print(f'CR | {self.n_commands} | {self.n_responses}')
                pass

    def _receive_thread(self):
        """
        Listens to responses from the drone.

        :return: None.
        """
        while True:
            if self.stop_thread:
                print('THREAD | RECEIVE | stopping')
                break
            
            try:
                response, ip = self.socket.recvfrom(1024)

                response = response.decode('utf-8').strip()
                ip = ''.join(str(ip[0]))                

                self.n_responses = self.n_responses + 1
                
                if response.upper() == 'OK' and not self.active:
                    # print(f'RESPONSE | {self.__repr__()} is active | {self.logs[-1].command} | {response} | {ip}')
                    print(f'RESPONSE | {self.__repr__()} is active | {response} | {ip}')
                    self.active = True
                else:
                    # print(f'RESPONSE | {self.__repr__()} | {self.logs[-1].command} | {response} | {ip}')
                    print(f'RESPONSE | {self.__repr__()} | {response} | {ip}')
                
                self.logs[-1].add_response(response, ip)
            except socket.error as e:
                # print(f'THREAD | RECEIVE | socket_error | {e}')
                pass
            finally:
                # print(f'CR | {self.n_commands} | {self.n_responses}')
                pass

if __name__ == '__main__':
    drones = [
        Drone(0, Address('192.168.3.101', 8889)),
        Drone(1, Address('192.168.3.103', 8889))
    ]

    commands = [
        '* > command',
        '* > battery?'
    ]

    swarm = Swarm(Address('', 8889), drones, commands)

    try:
        swarm.init()
        swarm.start()
        swarm.wait()
    except KeyboardInterrupt as ki:
        print('KEYBOARD INTERRUPT')
    except Exception as e:
        traceback.print_exc()
    finally:
        swarm.deinit()