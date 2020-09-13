import sys


def readline(length):
    if length:
        return list(map(int, sys.stdin.readline().rstrip().split(' ')))
    else:
        return int(sys.stdin.readline().rstrip())


def get_new_score(score, biggest):
    return score / biggest * 100


def main():
    N = readline(length=None)
    scores = readline(length=N)
    biggest = sorted(scores)[-1]
    score_sum = 0

    for score in scores:
        score_sum += get_new_score(score, biggest)

    print(score_sum / N)


main()
