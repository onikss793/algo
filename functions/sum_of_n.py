from functools import reduce


def solve(a: list) -> int:
    return reduce(lambda a, b: a + b, a)


arr = [1, 2, 3]
print(solve(arr))
