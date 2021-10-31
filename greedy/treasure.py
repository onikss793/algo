def get_input():
    N = int(input())
    A = map(int, input().split(' '))
    B = map(int, input().split(' '))

    return N, A, B


def main():
    N, A, B = get_input()

    sorted_a = list(reversed(sorted(A)))
    sorted_b = sorted(B)

    result = 0

    for i in range(N):
        result += sorted_a[i] * sorted_b[i]

    print(result)


if __name__ == '__main__':
    N = 9
    A = [5, 15, 100, 31, 39, 0, 0, 3, 26]
    B = [11, 12, 13, 2, 3, 4, 5, 9, 1]

    main()

# 5
# 1 1 1 6 0
# 2 7 8 3 1
# {1, 1, 0, 1, 6}
