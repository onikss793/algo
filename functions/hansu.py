def main():
    case = int(input())
    hansu = 0

    for n in range(1, case + 1):
        if n <= 99:
            hansu += 1
        else:
            if is_hansu(n):
                hansu += 1

    print(hansu)


def is_hansu(number):
    num_list = list(map(int, str(number)))

    return num_list[0] - num_list[1] == num_list[1] - num_list[2]


main()
