from datetime import datetime

class Stats:
    def __init__(self, command, id):
        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None

    def add_response(self, response):
        self.response = response
        self.end_time = datetime.now()
        self.duration = self.get_duration()

    def get_duration(self):
        diff = self.end_time - self.start_time
        return diff.total_seconds()

    def print_stats(self):
        print(f'\nid {self.id}')
        print(f'command: {self.command}')
        print(f'response: {self.response}')
        print(f'start_time: {self.start_time}')
        print(f'end_time: {self.end_time}')
        print(f'duration: {self.duration}')

    def got_response(self):
        if self.response is None:
            return False
        else:
            return True

    def return_stats(self):
        str = ''
        str +=  '\nid: %s\n' % self.id
        str += 'command: %s\n' % self.command
        str += 'response: %s\n' % self.response
        str += 'start time: %s\n' % self.start_time
        str += 'end_time: %s\n' % self.end_time
        str += 'duration: %s\n' % self.duration
        return str