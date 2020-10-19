def set_dict(word_dict, text):
    for n in text:
        if n in word_dict.keys():
            word_dict[n] += 1
        else:
            word_dict[n] = 1


def main():
    text = input().upper()
    word_dict = {}
    set_dict(word_dict, text)

    biggest_num = 0
    result = ''

    for key, value in word_dict.items():
        if biggest_num < value:
            biggest_num = value
            result = key
        elif biggest_num == value:
            result = '?'

    print(result)


main()
