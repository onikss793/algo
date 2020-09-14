def main():
    case = int(input())
    count = 0

    for number in range(1, case + 1):
        print(number)
        print(is_hansu(number))
        if is_hansu(number):
            count += 1

    print(count)
    return count


def is_hansu(number):
    units = list(map(int, str(number).split()))
    common_difference = units[1] - units[0] if len(units) > 1 else 0
    first_num = units[0]

    for n, unit in enumerate(units):
        ap = get_ap(n + 1, first_num, common_difference)

        if ap != unit:
            return False

    return True


def get_ap(n, first_num, common_diff):
    return first_num + (n - 1) * common_diff


main()
