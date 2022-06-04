from functools import reduce


def get_inputs():
    count = input()
    nums = input()

    return count, nums


def main():
    _, nums = get_inputs()

    result = reduce(lambda a, b: a + b, list(map(int, list(nums))))

    print(result)


main()
