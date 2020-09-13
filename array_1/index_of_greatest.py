import sys


def set_array(array: list):
    for n in range(9):
        number = int(sys.stdin.readline().rstrip())
        array.append(number)

    return array


def main():
    array = []
    set_array(array)
    biggest = 0

    for num in array:
        if num > biggest:
            biggest = num

    index = array.index(biggest) + 1

    print(biggest)
    print(index)


main()

# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61
