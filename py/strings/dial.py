def find_number(n):
    dial = {
        2: ['A', 'B', 'C'],
        3: ['D', 'E', 'F'],
        4: ['G', 'H', 'I'],
        5: ['J', 'K', 'L'],
        6: ['M', 'N', 'O'],
        7: ['P', 'Q', 'R', 'S'],
        8: ['T', 'U', 'V'],
        9: ['W', 'X', 'Y', 'Z']
    }

    for num, alphabets in dial.items():
        if n in alphabets:
            return num


def main():
    text = list(input())

    time = 0

    for n in text:
        number = find_number(n)
        time += number + 1

    print(time)


main()
