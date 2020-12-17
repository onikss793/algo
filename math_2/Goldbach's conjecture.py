import math


def cache_prime_number():
    cache = []

    for number in range(0, 10001):
        cache.append(is_prime_number(number))

    return cache


def is_prime_number(number: int) -> bool:
    if number == 1 or number == 0:
        return False

    standard = math.floor(math.sqrt(number))

    for n in range(2, standard + 1):
        if number % n == 0:
            return False

    return True


def main():
    cache = cache_prime_number()

    T = int(input())

    results = []

    for _ in range(T):
        n = int(input())

        half = n // 2

        for number in range(half, n + 1):
            if cache[number] and cache[n - number]:
                value = sorted([number, n - number])
                results.append(value)
                break

    [print(f'{number[0]} {number[-1]}') for number in results]


main()
