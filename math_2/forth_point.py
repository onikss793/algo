def get_rectangle(points):
    x = []
    y = []

    for point in points:
        x.append(point[0])
        y.append(point[-1])

    max_x = max(x)
    max_y = max(y)
    min_x = min(x)
    min_y = min(y)

    return [(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)]


def main():
    points = []

    for _ in range(3):
        x, y = map(int, input().split(' '))
        points.append((x, y))

    rectangle = get_rectangle(points)

    for point in points:
        rectangle.remove(point)

    x, y = rectangle[0]
    print(f'{x} {y}')


main()
