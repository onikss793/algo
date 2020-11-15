def main():
    x = int(input())
    stage, standard = get_stage(x)

    seq = x - standard - 1

    x, y = get_fraction(stage, seq)

    print(f"{x}/{y}")


def get_fraction(stage, seq):
    result = []

    if stage % 2 == 0:
        x = 1
        y = stage

        while x <= stage:
            result.append((x, y))
            x += 1
            y -= 1

    if stage % 2 != 0:
        x = stage
        y = 1

        while y <= stage:
            result.append((x, y))
            x -= 1
            y += 1

    return result[seq]


def get_stage(x):
    stage = 0
    result = 0
    result += stage

    while x > result:
        stage += 1
        result += stage

    return stage, result - stage


main()
