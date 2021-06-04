def pay(total: int, bill: int, count: int) -> int:
    if total <= 0:
        return total, count

    while total // bill > 0:
        total -= bill
        count += 1

    return total, count


def main():
    total = 1000 - int(input())
    count = 0
    bills = [500, 100, 50, 10, 5, 1]

    for bill in bills:
        total, count = pay(total, bill, count)

    print(count)


main()
