"""
분할 정복 (devide and cnoquer) + 재귀 
주어진 배열을 원소가 하나 밖에 남지 않을 때까지 둘로 쪼갠 후에 다시 값의 크기 순으로 재배열한다. 

퀵소트와 함께 빠른 정렬로 분류된다
퀵소트와는 반대로 안정 정렬에 속한다

* 시간 복잡도
평균, 최선, 최악의 경우 모두 O(nlogn)

Linked List 의 정렬이 필요할 때 합병 정렬을 사용하면 효율적이다. 
linked list 를 퀵정렬을 사용해 정렬하게 되면 순차 접근이 아닌 임의 접근을 하기 때문에 비효율적이다. 
반면 합병 정렬은 순차적으로 비교하기 때문에(배열의 시작부터 끝까지) Head -> 부터 탐색해야 하는 linked listdp gydbfwjrdlek
"""

# def merge_sort(arr):
#     if len(arr) < 2:  # 배열의 원소가 1개 남으면 return
#         return arr
#
#     mid = len(arr) // 2  # 가운데 값을 찾는다.
#     low_arr = merge_sort(arr[:mid])  # 가운데 값을 기준으로 왼쪽의 배열을 재귀
#     high_arr = merge_sort(arr[mid:])  # 가운데 값을 기준으로 오른쪽의 배열을 재귀
#
#     merged_arr = []
#
#     l = h = 0  # 각 배열의 index
#
#     while l < len(low_arr) and h < len(high_arr):  # 배열의 끝까지 반복을 돈다
#         if low_arr[l] < high_arr[h]:  # 양 배열의 값의 크기가 < 라면
#             merged_arr.append(low_arr[l])  # 작은 값을 병합한다
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])  # 양 배열의 값의 크기가 > 라면
#             h += 1  # 큰 값을 병합한다
#
#     merged_arr += low_arr[l:]  # low_arr 의 남은 값을 병합한다
#     merged_arr += high_arr[h:]  # high_arr 의 남은 값을 병합한다
#
#     return merged_arr


def merge_sort(arr: list):
    def sort(start, end):
        if end - start < 2:  # index 시작과 끝의 차가 2 미만이면 함수 정지
            return

        mid = (start + end) // 2  # 가운데 값을 구한다
        sort(start, mid)  # 왼쪽 배열 sort 재귀
        sort(mid, end)  # 오른쪽 배열 sort 재귀
        merge(start, mid, end)  # sort 가 완료되었으면 병합한다

    def merge(start, mid, end):
        print(start, mid, end)
        temp = []  # 임시 저장 배열
        s, e = start, mid  # 시작, 끝 index 를 저장해놓는다

        while s < mid and e < end:  # 시작 < 중간 and 중간 < 끝일 경우만 반복
            if arr[s] < arr[e]:  # 양 배열이 < 라면
                temp.append(arr[s])  # 왼쪽 값 병합
                s += 1  # 왼쪽 배열 인덱스 + 1
            else:  # 양 배열이 > 라면
                temp.append((arr[e]))  # 오른쪽 값 병합
                e += 1  # 오른쪽 배열 인덱스 + 1

        while s < mid:  # 오른쪽 배열만 반복이 끝나고 완쪽 배열만 남았을 경우
            temp.append(arr[s])  # 왼쪽 배열을 차례대로 병합한다
            s += 1
        while e < end:  # 왼쪽 배열만 병합이 끝나고 오른쪽 배열만 남았을 경우
            temp.append(arr[e])  # 오른쪽 배열을 차례대로 병합한다
            e += 1

        for i in range(start, end):  # 시작 -> 끝까지 반복
            arr[i] = temp[i - start]  # 임시 병합한 배열의 값을 실제 배열에 밀어넣는다

    return sort(0, len(arr))


arr = [6, 5, 7, 1, 8, 7, 2, 4]
result = merge_sort(arr)
print(arr)
