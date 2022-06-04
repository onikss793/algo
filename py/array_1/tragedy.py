import functools
import sys


def get_num_of_test_cases():
    return int(sys.stdin.readline().rstrip())


def get_student_number(raw_data):
    return raw_data[0]


def get_scores(raw_data):
    return raw_data[1:]


def get_average(scores):
    score_sum = functools.reduce(lambda a, b: a + b, scores)

    return score_sum / len(scores)


def print_tragedy():
    raw_data = list(map(int, sys.stdin.readline().rstrip().split(' ')))

    student_num = get_student_number(raw_data)
    scores = get_scores(raw_data)
    average = get_average(scores)
    num_over_avg = 0

    for score in scores:
        if score > average:
            num_over_avg += 1

    winners = (num_over_avg / student_num) * 100

    print('%.3f' % winners + '%')


def main():
    N = get_num_of_test_cases()

    for _ in range(N):
        print_tragedy()


main()
