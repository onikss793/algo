from typing import List


def solution(n: int, k: int):
    answer = -1

    number = convert_k_base(n, k)
    splited_number = split_number(number)

    prime_numbers = list(
        filter(
            lambda num: is_prime_number(num),
            splited_number
        )
    )

    print(prime_numbers)
    answer = len(prime_numbers)

    return answer


def match_every_conditions(num: int, origin: int):
    stringified_origin = str(origin)
    stringified_num = str(num)

    start_idx = stringified_origin.find(stringified_num)
    end_idx = start_idx + len(stringified_num)
    pass


def convert_k_base(num: int, base: int):
    tmp = ''

    while num:
        tmp = str(num % base) + tmp
        num //= base

    return tmp


def split_number(num: int) -> List[str]:
    stringified = str(num).split('0')

    return [int(num) for num in filter(lambda x: len(x), stringified)]


def is_prime_number(num: int) -> bool:
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return False if num <= 1 else True


res = solution(437674, 3)
print(res)
# 211020101011
