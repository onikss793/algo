import sys

line_number = int(sys.stdin.readline().rstrip())

for n in range(1, line_number + 1):
    blank = ' ' * (line_number - n)
    print(blank + ('*' * n))
