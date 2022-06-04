import sys


def get_numbers():
    arr = []

    for n in range(10):
        arr.append(int(sys.stdin.readline().rstrip()))

    return arr


def main():
    numbers = get_numbers()
    obj = {}

    for num in numbers:
        rest = str(num % 42)

        if rest in obj.values():
            obj[rest] += 1
        else:
            obj[rest] = 1

    print(len(obj.keys()))


main()
# 39
# 40
# 41
# 42
# 43
# 44
# 82
# 83
# 84
# 85