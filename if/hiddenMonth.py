year = int(input('Enter the year: '))


def getNumMultiple(subject):
    def isMultipleOf(number):
        return subject % number == 0

    return isMultipleOf


isYearMultipleOf = getNumMultiple(year)

print(
    1
    if (isYearMultipleOf(4) and isYearMultipleOf(100)) is False or (isYearMultipleOf(400))
    else 0
)
