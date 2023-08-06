import sys

try:
    with open('words.txt') as words:
        pass
except IOError as e:
    print(f'{e}\n Error opening words.txt. Terminating process', file=sys.stderr)
    sys.exit(1)
    