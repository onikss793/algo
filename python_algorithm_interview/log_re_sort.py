from pprint import pprint


def main():
    logs = ['dig1 1 8 1 5 1', 'let1 art can',
            'dig2 3 6', 'let2 own kit dog', 'let3 art zero']

    digits = []
    letters = []

    [
        digits.append(log)
        if log.split()[1].isdigit()
        else letters.append(log)
        for log in logs
    ]

    letters.sort(key=lambda letter: (letter.split()[1:], letter.split()[0]))
    # 파이썬 정렬에서는 sort 함수와 key 파라미터를 잘 활용하자, 순차적으로 정렬의 키값들을 지정해 줄 수 있음

    result = letters + digits

    pprint(result)

    pass


if __name__ == '__main__':
    main()
