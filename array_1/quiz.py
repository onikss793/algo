import sys


def read_number():
    return int(sys.stdin.readline().rstrip())


def read_ox():
    return sys.stdin.readline().rstrip()


def is_right(el):
    return el == 'O'


def main():
    N = read_number()
    total = 0

    for _ in range(N):
        ox = read_ox()
        score = 0

        for el in ox:
            if is_right(el):
                score += 1
            else:
                score = 0

            total += score

        print(total)
        total = 0


main()
