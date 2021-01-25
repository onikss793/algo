def main():
    N = int(input())
    number = 2

    while 1:
        if N == 1:
            break
        if N % number:
            number += 1
        else:
            print(number)
            N //= number


main()
