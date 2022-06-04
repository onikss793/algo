def check_right_triangle(_a, _b, _c):
    indexes = [_a, _b, _c]

    c = max(indexes)
    indexes.remove(c)

    a, b = indexes

    return a**2 + b**2 == c**2


def main():
    results = []

    while True:
        a, b, c = map(int, input().split(' '))

        if not a and not b and not c:
            break

        results.append('right' if check_right_triangle(a, b, c) else 'wrong')

    [print(result) for result in results]


main()
