import sys

test_numbers = int(sys.stdin.readline().rstrip())

for n in range(1, test_numbers + 1):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print(f'Case #{n}: {a + b}')
