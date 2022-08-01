import argparse
import sys

def calc(args):
    if args.o=='add':
        return args.x + args.y

    elif args.o=='sub':
        return args.x - args.y

    elif args.o=='mul':
        return args.x * args.y

    elif args.o=='div':
        return args.x / args.y
    else:
        return "Something Went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="Enter first number, this is utility for calculation")

    parser.add_argument('--y', type=float, default=3.0, help="Enter second number, this is utility for calculation")

    parser.add_argument('--o', type=str, default="add", help="this is utility for calculation")

    args = parser.parse_args()

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))   # calc ags will calculate the value that wht value is given then it will write in console after it, it will convert in string  

    # it will calculate the if we give the value in this form
    
# by this command we have to run this in cmd or pawer shell

    # python 93_utility_in_python.py --x 2 --y 6 --o add