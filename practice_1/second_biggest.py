import sys


def main():
    numbers = map(int, sys.stdin.readline().rstrip().split(' '))

    print(sorted(numbers)[1])


main()
