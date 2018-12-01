#!/usr/bin/env python3
import argparse

help_msg = '''
USAGE
  todo [-a] [-r] [-n NUMBER] [-c] [-h]

OPTIONAL ARGUMENTS
  -a                Add a task to the list

  -r                Remove a task

  -n NUMBER         Remove NUMBER of tasks

  -c                Clear the task list

  -h                Show this help message

LONG ARGUMENTS
  -a --add
  -r --remove
  -n --remove-number
  -c --clear
  -h --help
'''

parser = argparse.ArgumentParser(add_help=False,description='to-do list')

parser.add_argument('-a', '--add',
                    action='store_true',
                    help='add to the list')
parser.add_argument('-r', '--remove',
                    action='store_true',
                    help='remove a task')
parser.add_argument('-n', '--remove-number',
                    default=0, type=int,
                    help='remove NUMBER of tasks')
parser.add_argument('-c', '--clear',
                    action='store_true',
                    help='clear the list')
parser.add_argument('-h', '--help',
                    action='store_true',
                    help='show the help message')

args = parser.parse_args()

if args.help:
    print(help_msg)
    exit()


def main():
    if  args.add:
        print('name of the task to add:')

    if  args.remove:
        print('remove a task')

    if  (args.remove_number >= 1):
        print(args.remove_number)


if __name__ == '__main__':
    main()
