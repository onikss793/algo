def get_distance(a, b):
    return a - b


def main():
    x, y, w, h = map(int, input().split(' '))

    print(
        min([
            get_distance(x, 0),
            get_distance(w, x),
            get_distance(y, 0),
            get_distance(h, y)
        ])
    )


main()
