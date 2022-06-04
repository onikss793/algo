"""
완전 이진 트리를 기본으로 하는 Heap 자료 구조를 기반으로 한 정렬
완전 이진 트리?
  - 삽입할 때 왼쪽부터 차례대로 추가하는 이진 트리
시간 복잡도는 O(nlogn)

1. 최대 힙을 구성
2. 현재 힙 루트는 가장 큰 값이 존재함. 루트의 값을 마지막 요소와 바꾼 후, 힘의 사이즈 하나 줄임
3. 힙의 사이즈가 1보다 크면 위 과정 반복
"""


def heapify(unsorted, index, heap_size):
    print('unsorted : ', unsorted)

    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    print('before max heap : ', unsorted)

    n = len(unsorted)

    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)

    print('*' * 100)
    print('after max heap', unsorted)
    print('*' * 100)

    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)

    return unsorted


arr = [4, 2, 5, 1, 2, 6, 3]

heap_sort(arr)

