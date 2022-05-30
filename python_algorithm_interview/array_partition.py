inputs = [1, 4, 3, 2]


def main():
    result = sum(sorted(inputs)[::2])
    print(result)


if __name__ == '__main__':
    main()

# answer: 4
