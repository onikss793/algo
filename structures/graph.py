class Node:
    def __init__(self):
        self.index = 0
        self.distance = 0
        self.next = None

    def set(self, index, distance, next):
        self.index = index
        self.distance = distance
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = Node()

    def add_front(self, index, distance):
        node = Node()
        node.set(index, distance, self.root.next)
        self.root.next = node

    def show_all(self):
        curr = self.root.next

        while curr:
            print(f"{curr.index}(거리: {curr.distance}) ", end='')
            curr = curr.next


def main():
    n, m = map(int, input().split(" "))  # n은 노드 갯수, m은 간선의 갯수
    a = [LinkedList() for _ in range(n+1)]

    for _ in range(m):
        x, y, distance = map(int, input().split(" "))
        node = a[x]
        node.add_front(y, distance)

    for i in range(len(a)):
        print(f"원소 [{i}]", end=' ')
        a[i].show_all()
        print('', end='\n')

    pass

# def main():
#     n, m = map(int, input().split(' '))
#     # n 은 노드 갯수, m 은 간선의 갯수
#     a = [[0 for _ in range(n)] for _ in range(n)]
#
#     for r in a:
#         print(f"{r}", end='\n')
#
#     for _ in range(m):
#         x, y = map(int, input().split(' '))
#         # x 노드와 y 노드의 간선을 표시
#         a[x-1][y-1] = 1
#         a[y-1][x-1] = 1
#
#     for i, x in enumerate(a):
#         for j, y in enumerate(x):
#             print(f"{a[i][j]}", end=' ')
#         print('', end='\n')


main()
