import sys
import argparse
from swarm import *

def parse_args(args):
    """
    Parses arguments.
    :param args: Arguments.
    :return: Arguments.
    """
    parser = argparse.ArgumentParser('planned-flight.py', 
                    epilog='One-Off Coder http://www.oneoffcoder.com')

    parser.add_argument('-f', '--file', help='Command text file', required=True)
    parser.add_argument('--version', action='version', version='%(prog)s v0.0.1')

    return parser.parse_args(args)

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    fpath = args.file

    swarm = Swarm(fpath)
    swarm.start()
