def solution(s: str):
    answer = 0
    count = 2

    while count <= len(s):
        words = []
        for i in range(count):
            words.append(s[i:i + count])

        count += 1

        print(words)
    return answer


res = solution("aabbaccc")
print(res)
