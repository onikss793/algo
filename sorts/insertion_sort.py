def main():
    n = int(input())
    arr = [None] * n

    for i in range(n):
        arr[i] = int(input())

    for i in range(n - 1):
        j = i

        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

    [print(d) for d in arr]


main()

# def main(arr: list):
#     for i in range(1, len(arr)):
#         temp = arr[i]
#         prev = i - 1
#
#         while prev >= 0 and arr[prev] > temp:
#             arr[prev+1] = arr[prev]
#             prev -= 1
#             print(temp, arr[prev], arr[prev+1])
#         arr[prev+1] = temp
#
#     print(arr)
#
# arr = [21, 36, 3, 76, 8, 36, 97, 75, 2, 7, 79]
#
# print(arr)
# main(arr)
