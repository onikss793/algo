def main():
    n, word = input().split(" ")
    words = []
    founded = 0

    for _ in range(int(n)):
        words.append(input())

    for index, value in enumerate(words):
        if value == word:
            print(f"{index + 1}번째 원소입니다. ")
            founded = 1

    if founded == 0:
        print("원소를 찾을 수 없습니다. ")


main()
