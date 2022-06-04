import sys


def main():
    number = int(sys.stdin.readline().rstrip())

    for n in range(1, number + 1):
        print('*' * n)

    for n in reversed(range(number)):
        print('*' * n)


main()
