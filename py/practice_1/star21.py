import sys


def draw_star(num):
    return '*' if num else ' '


def is_odd(num):
    return num % 2 != 0


def draw_odd(num):
    array = []

    for n in range(1, num + 1):
        array.append(1) if is_odd(n) else array.append(0)

    print(''.join(map(draw_star, array)))


def draw_even(num):
    array = []

    for n in range(1, num + 1):
        array.append(1) if is_odd(n) is False else array.append(0)

    print(''.join(map(draw_star, array)))


def draw_set(number):
    for n in range(1, (number * 2) + 1):
        if is_odd(n):
            draw_odd(number)
        else:
            draw_even(number)


def main():
    number = int(sys.stdin.readline().rstrip())

    draw_set(number)


main()
