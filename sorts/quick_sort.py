def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    l_arr, eq_arr, gt_arr = [], [], []

    for num in arr:
        if num < pivot:
            l_arr.append(num)
        elif num > pivot:
            gt_arr.append(num)
        else:
            eq_arr.append(num)

    return quick_sort(l_arr) + eq_arr + quick_sort(gt_arr)

result = quick_sort([3, 8, 5, 4, 6, 9, 1, 0, 7, 2])

print(result)

