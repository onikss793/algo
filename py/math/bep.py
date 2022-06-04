def get_inputs():
    A, B, C = list(map(int, input().split(' ')))

    return A, B, C


def get_minimum_count(A, B, C):
    return (A // C) + (B // C)


def get_total(C):
    def result(count):
        return C * count

    return result


def main():
    A, B, C = get_inputs()

    minimum_count = get_minimum_count(A, B, C)
    count = minimum_count + ((A & C) + (B % C)) // C  # 나머지들의 합에서 최대의 C
    total_price = get_total(C)

    total = total_price(count)

    while total < A + B * C:
        count += 1
        total = total_price(count)

    print(count + 1)


# main()


def init():
    # A 고정비용
    # B 1대 당 생산비
    # C 1대 당 가격
    # count 갯수
    # profit = (C - B) * count - A
    # profit > 0
    # (C - B) * count - A > 0
    # count > A / (C - B)
    # 갯수는 해당 식보다 하나만 많으면 무조건 손익분기점을 넘게 된다. 
    # 그러므로 count 는 A // (C - B) + 1 

    A, B, C = map(int, input().split())

    if B >= C:
        print(-1)
    else:
        print(A // (C - B) + 1)


init()


