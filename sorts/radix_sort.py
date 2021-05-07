def counting_sort(arr, digit):
    n = len(arr)

    output = [0 for _ in range(n)]
    count = [0 for _ in range(10)]

    for i in range(0, n):
        index = int(arr[i] / digit)
        count[index % 10] += 1
        
    i = n - 1

    while i >= 0:
        index = int(arr[i] / digit)
        output[count[(index) % 10] - 1] = arr[i]
        count[index%10] -= 1
