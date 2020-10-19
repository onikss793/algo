def get_result():
    strings = input().split(' ')
    count = int(strings[0])
    text = strings[1]

    result = []

    for character in text:
        result.append(character * count)

    return ''.join(result)


def main():
    test_case_count = int(input())

    for n in range(test_case_count):
        print(get_result())


main()
