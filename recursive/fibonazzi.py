# def get_fibonazzi(default=21):
#     cache = [0 for _ in range(default)]
#     cache[1] = 1
#
#     for i in range(2, default):
#         cache[i] = cache[i - 1] + cache[i - 2]
#
#     return cache
#
#

def fibonazzi(default=20):
    cache = [-1 for _ in range(default + 1)]

    def fibo(n):
        if n < 2:
            return n

        if cache[n] != -1:
            return cache[n]

        cache[n] = fibo(n - 1) + fibo(n - 2)

        return cache[n]

    fibo(default)
    cache[0] = 0
    cache[1] = 1

    return cache


def main():
    N = int(input())

    cache = fibonazzi()

    print(cache[N])


main()
