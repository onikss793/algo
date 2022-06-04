def get_croatia_alphabets():
    croatia_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    return croatia_alphabets


def get_word_recursively(words, alphabet, count, length):
    if words.find(alphabet) != -1:
        count += 1
        length += len(alphabet)

        start_index = words.find(alphabet)
        end_index = start_index + len(alphabet)

        new_words = words[:start_index] + words[end_index:]

        return get_word_recursively(new_words, alphabet, count, length)
    else:
        return count, length


def main():
    words = input().strip()

    croatia_alphabets = get_croatia_alphabets()
    while True:
        temp = words

        for character in croatia_alphabets:
            if character in temp:
                index = temp.index(character) # 문자열에서 croatia 특수문자가 시작하는 인덱스
                len_of_croatia_word = len(character) # croatia 특수문자 길이
                temp = temp[:index] + '/' + temp[index + len_of_croatia_word:] # 특수문자 하나를 "/"로 교체
                break
        if temp != words:
            s = temp
        else:
            break

    print(len(words))


# main()

def init():
    croatia_alphabets = get_croatia_alphabets()

    strings = input()

    for croatia_alphabet in croatia_alphabets:
        strings = strings.replace(croatia_alphabet, '*')

    print(len(strings))


init()

# ljes=njak
