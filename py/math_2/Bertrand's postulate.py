import math


def is_prime_number(number: int) -> bool:
    if number == 1 or number == 0:
        return False

    standard = math.floor(math.sqrt(number))

    for n in range(2, standard + 1):
        if number % n == 0:
            return False

    return True


def cache_prime_number():
    cache = []
    standard = 123456

    for number in range(0, standard * 2 + 1):
        cache.append(is_prime_number(number))

    return cache


def main():
    cache = cache_prime_number()
    results = []

    while True:
        n = int(input())
        N = 2 * n

        if n == 0:
            break

        results.append(sum(cache[n+1:N+1]))

    [print(count) for count in results]


main()
