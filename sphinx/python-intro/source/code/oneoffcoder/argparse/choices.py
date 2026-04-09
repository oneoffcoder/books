import argparse

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['fast', 'safe', 'debug'])
args = parser.parse_args()

print(f'mode={args.mode}')
