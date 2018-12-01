#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='to-do list')

parser.add_argument('-a', '--add',
                    action='store_true',
                    help='add to the list')
parser.add_argument('-r', '--remove',
                    action='store_true',
                    help='remove from the list')
args = parser.parse_args()



def main():
    if args.add:
        print('name of the task to add:')
    if args.remove:
        print('task to remove:')




if __name__ == '__main__':
    main()
