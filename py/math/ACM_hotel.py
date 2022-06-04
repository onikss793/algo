from math import ceil


test_cases = input()
result = []

for _ in range(int(test_cases)):
    H, W, N = map(int, input().split(' '))

    floor = H * 100 if not N % H else (N % H) * 100
    no = int(ceil(N / H))

    result.append(floor + no)


[print(r) for r in result]
