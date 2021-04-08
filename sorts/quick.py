"""
* 시간 복잡도
최선의 경우, nlog2n
최악의 경우 O(n^2) : 이미 오름차순이나 내림차순 정렬이 되어 있는 경우

* 공간 복잡도
주어진 배열 안에서 swap 할 경우 O(n)

* 장점
불필요한 데이터의 이동을 줄이고 먼 거리의 데이터를 교환할 수 있다. 
한번 결정된 피벗들이 추후 연상에서 제외되기 때문에 O(nlog2n)을 가지는 다른 정렬 알고리즘과 비교했을 때도 가장 빠르다. 

* 단점
불안정 정렬
이미 정렬된 배열에 대해서는 오히려 수행시간이 더 많이 걸릴 수 있다. 
"""

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]
#
#     lesser_arr, equal_arr, greater_arr = [], [], []
#
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


def quick_sort(arr) -> list:
    def sort(low: int, high: int):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low: int, high: int) -> int:
        pivot = arr[(low + high) // 2]

        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    sort(0, len(arr) - 1)

    return arr


arr = [6, 5, 1, 4, 7, 2, 3]
# [3, 5, 1, 4, 7, 2, 6]
# [3, 2, 1, 4, 7, 5, 6]
# [3, 2, 1] [4, 7, 5, 6]
# [1, 2, 3]
# [1] [2, 3]
# [1] [2] [3]
# [4, 5, 7, 6]
# [4, 5] [7, 6]
# [4] [5] [6, 7]
# [6] [7]
# [1, 2, 3, 4, 5, 6, 7]

result = quick_sort(arr)
print(result)
