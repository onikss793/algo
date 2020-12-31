import math


def is_prime_number(number: int) -> bool:
    if number == 1 or number == 0:
        return False

    standard = math.floor(math.sqrt(number))

    for n in range(2, standard + 1):
        if number % n == 0:
            return False

    return True


def main():
    M, N = map(int, input().split(' '))

    for number in range(M, N + 1):
        if is_prime_number(number):
            print(number)


main()
