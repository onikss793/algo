import math
import sys


def set_array(number, array: list):
    if number > 0:
        array.append(number)
        set_array(number - 2, array)
    else:
        return


def main():
    num = int(sys.stdin.readline().rstrip())
    count = num * 2 - 1
    array = []
    set_array(count, array)
    reversed_array = list(reversed(array))

    for n in array:
        blank = math.ceil(((count - n) / 2)) * ' '
        print(blank + '*' * n)

    for n in reversed_array[1:]:
        blank = math.ceil(((count - n) / 2)) * ' '
        print(blank + '*' * n)


main()
