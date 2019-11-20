from datetime import datetime

class Stats(object):
    def __init__(self, command, id):
        """
        Constructor.
        :param command: The command sent.
        :param id: The identifier.
        """
        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None

    def add_response(self, response):
        """
        Adds the response.
        :param response: Response.
        :return: None.
        """
        self.response = response
        self.end_time = datetime.now()
        self.duration = self.get_duration()

    def get_duration(self):
        """
        Gets the duration.
        :return: Duration.
        """
        diff = self.end_time - self.start_time
        return diff.total_seconds()

    def print_stats(self):
        """
        Prints the statistics.
        :return: None.
        """
        print(f'\nid {self.id}')
        print(f'command: {self.command}')
        print(f'response: {self.response}')
        print(f'start_time: {self.start_time}')
        print(f'end_time: {self.end_time}')
        print(f'duration: {self.duration}')

    def got_response(self):
        """
        Returns a boolean if a response was received.
        :return: Boolean.
        """
        
        if self.response is None:
            return False
        else:
            return True

    def return_stats(self):
        """
        Returns the statistics.
        :return: Statistics.
        """
        str = ''
        str +=  f'\nid: {self.id}\n'
        str += f'command: {self.command}\n'
        str += f'response: {self.response}\n'
        str += f'start_time: {self.start_time}\n'
        str += f'end_time: {self.end_time}\n'
        str += f'duration: {self.duration}\n'
        return str