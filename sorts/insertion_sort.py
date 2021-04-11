def main(arr: list):
    for i in range(1, len(arr)):
        temp = arr[i]
        prev = i - 1

        while prev >= 0 and arr[prev] > temp:
            arr[prev+1] = arr[prev]
            prev -= 1
            print(temp, arr[prev], arr[prev+1])
        arr[prev+1] = temp

    print(arr)

arr = [21, 36, 3, 76, 8, 36, 97, 75, 2, 7, 79]

print(arr)
main(arr)


