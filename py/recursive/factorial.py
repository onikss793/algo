def get_factorial(N):
    case = [0, 1]
    return 1 if N in case else N * get_factorial(N - 1)


def main():
    N = int(input())

    print(get_factorial(N))


main()
