import sys


sys.setrecursionlimit(10**5)

def main():
    N = int(input())

    recursive(N)


def recursive(N, count=1):
    if N <= 1:
        print(count)
        return
    else:
        recursive(N - (6 * count), count + 1)

main()

