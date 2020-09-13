import sys


def get_number():
    number = 1

    for n in range(3):
        number = number * int(sys.stdin.readline().rstrip())

    return number


def get_num_dict():
    return {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
    }


def main():
    num_obj = get_num_dict()

    numbers = str(get_number())

    for n in numbers:
        num_obj[n] += 1

    for num in num_obj:
        print(num_obj[num])


main()
