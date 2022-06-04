def main(arr: list):
    temp = 0

    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp

    print(arr)

main([4, 1, 2, 26, 63, 95, 85, 45, 65, 75])

