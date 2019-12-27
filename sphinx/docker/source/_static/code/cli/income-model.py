import sys
import argparse

def parse_args(args):
    parser = argparse.ArgumentParser('Income Predictor', 
        epilog='One-Off Coder https://www.oneoffcoder.com')
    
    parser.add_argument('-e', '--education', 
        help='Years of education', 
        required=False, 
        default=0, 
        type=int)

    parser.add_argument('-v', '--version', action='version', version='%(prog)s v0.0.1')

    return parser.parse_args(args)

def predict(e):
    y = 25000.0 + 20000.0 * e
    return y

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    
    e = args.education
    e = 0 if e < 0 else e
    e = 20 if e > 20 else e

    y = predict(e)

    print(f'Esimated Income with {e} years past high school is is ${y:,.2f}')