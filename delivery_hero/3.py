# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    result = N + 1

    while True:
        if check(result) == False:
            result += 1
        else:
            break

    return result


def check(number: int) -> bool:
    # 같은 숫자가 하나라도 있으면 return False
    stringified = str(number)

    for i in range(len(stringified) - 1):
        num = int(stringified[i])
        next_num = int(stringified[i+1])

        if abs(num - next_num) == 0:
            return False

    return True


result = solution(44432)
print(result)
