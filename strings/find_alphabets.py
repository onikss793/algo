def get_alphabets():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def set_alphabets(alphabets):
    def convert_index(character):
        return alphabets.index(character)

    return convert_index


def set_text(text):
    # noinspection PyBroadException
    def convert_to_index(character):
        try:
            index = text.index(character)
        except:
            index = -1

        return index

    return convert_to_index


def main():
    text = list(input())

    convert_to_index = set_text(text)
    result = ' '.join(map(str, map(convert_to_index, get_alphabets())))
    print(result)


main()
