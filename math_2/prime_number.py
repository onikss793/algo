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
    M = int(input())
    N = int(input())

    result = []

    for number in range(M, N + 1):
        prime_number = is_prime_number(number)

        if prime_number:
            result.append(number)

    if not len(result):
        print(-1)
        return

    print(sum(result))
    print(result[0])


main()
