def main():
    number_of_trial = int(input())
    words = []
    result = 0

    for n in range(number_of_trial):
        words.append(input().strip())

    for word in words:
        count = count_group_character(word)
        if count == len(word):
            result += 1

    print(result)


def count_group_character(word):
    length = len(word)
    count = 0

    for n in range(length):
        character = word[n] # 단어의 글자를 차례대로 character에 저장한다

        if character in word[n + 1:]:    # character 다음에 똑같은 글자가 있다면?
            if word[n + 1] != character: # character 다음 글자가 character 와 다르다면?
                break                    # 더 이상 그룹이 아니다
            else:                        # character 다음 글자가 character 와 같은 글자라면?
                count += 1               # 같은 그룹이다 따라서count + 1
        else:
            count += 1                   # character 다음에 똑같은 글자가 없다면? 그 자체로 그룹 단어임

    return count


main()

