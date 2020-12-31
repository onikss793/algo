from math import sqrt


def get_c(x1, y1, x2, y2):
    return sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)


def is_same_x_y(x1, y1, x2, y2):
    return x1 == x2 and y1 == y2


def main():
    cases = int(input())

    results = []

    for _ in range(cases):
        x1, y1, r1, x2, y2, r2 = map(float, input().split(' '))

        if is_same_x_y(x1, y1, x2, y2):
            if r1 == r2:
                results.append(-1)
                continue
            else:
                results.append(0)
                continue

        c = get_c(x1, y1, x2, y2)

        distance = r1 + r2
        diff = abs(r1 - r2)

        if c == distance:
            results.append(1)
            continue
        elif c > distance:
            results.append(0)
            continue
        elif c < distance:
            if diff > c:
                results.append(0)
            elif diff < c:
                results.append(2)
            else:
                results.append(1)
            continue

    [print(result) for result in results]


main()
