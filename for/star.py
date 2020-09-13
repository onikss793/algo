import sys

line_number = int(sys.stdin.readline().rstrip())
star = '*'

for n in range(1, line_number+ 1):
    print(star * n)
