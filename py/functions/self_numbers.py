def main():
    case = 10000
    original = set(range(1, case + 1))
    d_nums = set(num + sum(int(units) for units in str(num)) for num in range(1, case + 1))

    self_numbers = sorted(list(set(original - d_nums)))

    [print(number) for number in self_numbers]


main()
