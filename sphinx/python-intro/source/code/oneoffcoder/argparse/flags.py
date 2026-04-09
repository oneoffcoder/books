import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()

if args.verbose:
    print('verbose mode enabled')
else:
    print('verbose mode disabled')
