for _ in range(int(input())):
    k = int(input())
    n = int(input())

    base = [i for i in range(1, n + 1)]

    for _ in range(k):
        for index in range(1, n):
            base[index] += base[index - 1]

    print(base[n - 1])
