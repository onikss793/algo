x = int(input())
y = int(input())


def isNumUnsigned(num):
    return num > 0


if isNumUnsigned(x) and isNumUnsigned(y):
    print(1)
elif isNumUnsigned(x) is False and isNumUnsigned(y):
    print(2)
elif isNumUnsigned(x) is False and isNumUnsigned(y) is False:
    print(3)
elif isNumUnsigned(x) and isNumUnsigned(y) is False:
    print(4)
