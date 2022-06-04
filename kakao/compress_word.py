def split_words_with_n(n, word):
    split_words = []
    split_word = ''

    for alphabets in word:
        split_word += alphabets

        if len(split_word) == n:
            split_words.append(split_word)
            split_word = ''

    if len(''.join(split_words)) != len(word):
        start_index = len(word) - len(''.join(split_words))
        split_words.append(word[-1 * start_index:])

    return split_words


def compress(n: int, word: str):
    result = ' ' * n
    split_words = split_words_with_n(n, word)

    for i in range(len(split_words)):
        alphabet_1 = split_words[i]
        letter_count = 1

        for j in range(i + 1, len(split_words)):
            alphabet_2 = split_words[j]

            if alphabet_1 == alphabet_2:
                letter_count += 1
            else:
                break

        letter_count = '' if letter_count == 1 else str(letter_count)

        if alphabet_1 != result[-n]:
            result += str(letter_count) + alphabet_1
    print(result) if n == 8 else None
    return result[n:]


def solution(s):
    answer = 1001

    for i in range(1, len(s) + 1):
        compressed_word = compress(i, s)
        print(compressed_word) if i == 8 else None
        if len(compressed_word) and len(compressed_word) < answer:
            answer = len(compressed_word)

    return answer


s = input()
print(solution(s))
