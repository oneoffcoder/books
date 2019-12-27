import os
from os import listdir
from os.path import isfile, join
import argparse
import sys

def replace_values(file_path, env_vals):
    count_matches = lambda s, k: s.count(k, 0, len(s)) 
    
    with open(file_path, 'r') as f:
        print('processing {}'.format(file_path))
        s = f.read()
        for key, val in env_vals.items():
            n = count_matches(s, key)
            if n > 0:
                print('\t{} matched {} times'.format(key, n))
                s = s.replace(key, val)
        return s

def save_file(file_path, s):
    with open(file_path, 'w') as f:
        f.write(s)

def get_file_paths(dir_path):
    files = (f for f in listdir(dir_path) if isfile(join(dir_path, f)))
    files = filter(lambda f: f.endswith('.js') or f.endswith('.map'), files)
    files = map(lambda f: join(dir_path, f), files)

    return files

def get_env_vals():
    get_value = lambda key, def_val: os.getenv(key, def_val)

    def_vals = {
        'ENV_SERVICE_URL': 'NONE',
        'ENV_API_KEY': 'NONE'
    }

    return {key: get_value(key, def_vals[key]) for key in def_vals.keys()}

def parse_args(args):
    parser = argparse.ArgumentParser('Externalize Angular Values')
    
    parser.add_argument('-d', '--dir', 
        help='directory with Angular files are located', 
        required=False,
        default='/usr/share/nginx/html')
    
    parser.add_argument('-v', '--version', action='version', version='%(prog)s v0.0.1')

    return parser.parse_args(args)

def main(args):
    env_vals = get_env_vals()

    file_paths = get_file_paths(args.dir)
    
    for file_path in file_paths:
        s = replace_values(file_path, env_vals)
        save_file(file_path, s)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args)