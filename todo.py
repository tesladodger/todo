#!/usr/bin/env python3
import argparse

help_msg = '''
USAGE
  todo [-l] [-a] [-r] [-n NUMBER] [-c] [-h]

OPTIONAL ARGUMENTS
  -l                List tasks

  -a                Add a task to the list

  -r                Remove a task

  -n NUMBER         Remove NUMBER of tasks

  -c                Clear the task list

  -h                Show this help message

LONG ARGUMENTS
  -l --list
  -a --add
  -r --remove
  -n --remove-number
  -c --clear
  -h --help
'''

parser = argparse.ArgumentParser(add_help=False,description='to-do list')

parser.add_argument('-l', '--list',
                    action='store_true',
                    help='list tasks')
parser.add_argument('-a', '--add',
                    action='store_true',
                    help='add a task')
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
    try:    # Create file if it doesn't exist
        file = open('tasks.txt', 'r')
    except FileNotFoundError:
        file = open('tasks.txt', 'w')
        file.close()


    if  args.list:
        file = open('tasks.txt', 'r')
        print('\n')
        num_of_lines = 0
        for line in file:
            num_of_lines += 1
            line = str(num_of_lines) + ' - ' + line
            print(line)
        if (num_of_lines == 0):
            print('  Nothing to do.')
            print('  Use \'todo -a\' to add a task')
        file.close()


    if  args.add:
        print('\n  Description of the task:')
        task_to_add = str(input('-> ')) + '\n'
        file = open('tasks.txt', 'a')
        file.write(task_to_add)


    if  args.remove:
        print('remove a task')

    if  (args.remove_number >= 1):
        print(args.remove_number)


if __name__ == '__main__':
    main()
