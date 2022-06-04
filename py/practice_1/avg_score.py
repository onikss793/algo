import sys


def get_number_from_line():
    number = int(sys.stdin.readline().rstrip())

    return number


def is_under_forty(number):
    return number < 40


def get_score(number):
    return number if is_under_forty(number) is False else 40


def main():
    num_students = 5
    sum_score = 0

    for n in range(5):
        number = get_number_from_line()
        score = get_score(number)
        sum_score += score

    print(int(sum_score / num_students))


main()
