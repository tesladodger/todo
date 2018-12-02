@echo off
doskey todo=py -3 todo.py $*
doskey q=exit $*
echo. && echo use 'todo -h' for help
