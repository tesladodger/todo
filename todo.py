#!/usr/bin/env python3
import argparse
import fileinput
from shutil import copyfile

help_msg = '''
USAGE
  todo [-l] [-a] [-r] [-n NUMBER] [-c] [-h]

OPTIONAL ARGUMENTS
  -l                List tasks

  -a                Add a task to the list

  -r                Remove a task

  -n NUMBER         Add NUMBER of tasks

  -c                Clear the task list

  -b                Backup the task list

  -h                Show this help message

LONG ARGUMENTS
  -l --list
  -a --add
  -r --remove
  -n --add-number
  -c --clear
  -b --backup
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
parser.add_argument('-n', '--add-number',
                    default=0, type=int,
                    help='remove NUMBER of tasks')
parser.add_argument('-c', '--clear',
                    action='store_true',
                    help='clear the list')
parser.add_argument('-b', '--backup',
                    action='store_true',
                    help='backup the list')
parser.add_argument('-h', '--help',
                    action='store_true',
                    help='show the help message')

args = parser.parse_args()

if args.help:
    print(help_msg)
    exit()


def print_tasks():  # Display tasks on screen
    file = open('tasks.txt', 'r')
    print('')
    num_of_lines = 0
    for line in file:
        line = str(num_of_lines) + ' - ' + line
        print(line)
        num_of_lines += 1
    if (num_of_lines == 0):
        print('  Nothing to do. Use \'todo -a\' to add a task')
    file.close()


def add_task():  # Add a task to the file
    print('\n  Description of the task:')
    task_to_add = str(input('-> ')) + '\n'
    file = open('tasks.txt', 'a')
    file.write(task_to_add)
    file.close()


def main():
    try:    # Create file if it doesn't exist
        file = open('tasks.txt', 'r')
    except FileNotFoundError:
        file = open('tasks.txt', 'w')
        file.close()


    if  args.list:  # Display tasks
        print_tasks()


    if  args.add:  # Add a task
        add_task()


    if  args.remove:  # Remove a task
        print_tasks()
        try:
            x = int(input('Number of the task to delete:\n -> '))
        except ValueError:
            print('Inut must be a valid integer')
        for line in fileinput.input('tasks.txt', inplace=True):
            if fileinput.lineno() == x+1:
                continue
            print(line, end='')


    if  (args.add_number >= 1):  # Add number of tasks
        for i in range(args.add_number):
            add_task()


    if args.clear:  # Clear all tasks
        x = str(input('\nDelete all tasks? [Y/n] '))
        if x == 'y' or x == 'Y':
            file = open('tasks.txt', 'w')
            file.write('')
            file.close()


    if args.backup:
        dstin = str(input('\nName of the backup file:\n -> ')) + '.txt'
        dstin = dstin.replace(' ','')
        sauce = 'tasks.txt'
        copyfile(sauce, dstin)
        print('  File saved as', dstin)


if __name__ == '__main__':
    main()
