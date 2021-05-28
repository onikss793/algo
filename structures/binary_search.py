NOT_FOUND = -9999


def search(numbers: list, start: int, end: int, target: int):
    if start > end:
        return NOT_FOUND

    mid = int((start + end) / 2)
    mid_number = numbers[mid]

    if mid_number == target:
        return mid
    elif mid_number > target:
        return search(numbers, start, mid - 1, target)
    else:
        return search(numbers, mid + 1, end, target)


def main():
    n, target = map(int, input().split(' '))
    numbers = []

    for _ in range(n):
        numbers.append(int(input()))

    result = search(numbers, 0, n - 1, target)

    if result != NOT_FOUND:
        print(f"{result+1} 번째 원소입니다. ")
    else:
        print("원소를 찾을 수 없습니다. ")


main()
