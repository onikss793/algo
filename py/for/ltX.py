import sys

N, X = map(int, sys.stdin.readline().rstrip().split(' '))
array = map(int, sys.stdin.readline().rstrip().split(' '))

result = []
for n in array:
    result.append(str(n)) if n < X else None

print(' '.join(result))
