from .time_check import time_check


def pointer_reverse():
    l = [1, 2, 3, 4, 5]

    left, right = l[0], len(l) - 1

    while left > right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right += 1

    print(l)


def index_reverse():
    l = [1, 2, 3, 4, 5]
    l[::-1]

    print(l)


def reverse_func():
    l = [1, 2, 3, 4, 5]
    l.reverse()

    print(l)


time_check(reverse_func)
time_check(index_reverse)
time_check(pointer_reverse)
