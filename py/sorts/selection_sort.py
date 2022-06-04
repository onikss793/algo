def main():
    array = []

    n = int(input())

    for _ in range(n):
        array.append(int(input()))

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        array[min_index], array[i] = array[i], array[min_index]

    print(array)


main()

# def main(arr: list):
#     min_index: int
#     temp: int
#
#     for i in range(len(arr)):
#         min_index = i
#
#         for j in range(i+1, len(arr)):
#             if (arr[j] < arr[min_index]):
#                 min_index = j
#
#
#         temp = arr[min_index]
#         arr[min_index] = arr[i]
#         arr[i] = temp
#
#     print(arr)

# main([12, 43, 643, 64, 34, 7, 67, 37, 895, 34, 786])
