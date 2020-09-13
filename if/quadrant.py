x = int(input())
y = int(input())


def isNumUnsigned(num):
    return num > 0


if isNumUnsigned(x) and isNumUnsigned(y):
    print(1)
elif not isNumUnsigned(x) and isNumUnsigned(y):
    print(2)
elif not isNumUnsigned(x) and not isNumUnsigned(y):
    print(3)
elif isNumUnsigned(x) and not isNumUnsigned(y):
    print(4)
