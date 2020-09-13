# 최소 2가지 이상의 단품 메뉴
# 최소 2명의 손님이 시킨 단품메뉴 조합


# INPUT: 알파벳이 담김 배열
# OUTPUT: 알파벳이 담긴 배열
# BLACKBOX: 가장 많이 등장한 알파벳들끼리의 조합을 알파벳 오름차순으로 정렬한다.
def solution(orders, course):
    alphabet_obj = {}
    answer = []

    for order in orders:
        make_object(order, alphabet_obj)

    print(order_alphabets(alphabet_obj))

    return answer


def make_object(alphabets: str, obj: dict):
    for al in alphabets:
        if al in obj:
            obj[al] += 1
        else:
            obj[al] = 1

    return obj


def order_alphabets(alphabet_obj):
    return sorted(alphabet_obj.values())


def get_nth_biggest_amount(alphabet_obj: dict, n: int):
    result = []


print('RESULT: ', solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
