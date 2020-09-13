def get_line():
    return map(int, input().split(' '))


def not_zero(a, b):
    return a != 0 and b != 0


def print_line():
    a, b = get_line()

    if not_zero(a, b):
        print(a + b)
        print_line()
    else:
        return None


print_line()
