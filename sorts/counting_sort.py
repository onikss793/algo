def main():
    MAX_VALUE = 1000001

    n = int(input())

    a = [0 for _ in range(MAX_VALUE)]

    for value in map(int, input().split(' ')):
        a[value] += 1

    for index, value in enumerate(a):
        while value:
            print(index, end=' ')
            value -= 1


main()
