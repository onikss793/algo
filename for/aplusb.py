import sys

test_numbers = int(sys.stdin.readline().rstrip())

for n in range(test_numbers):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))

    print(a + b)
