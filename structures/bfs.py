from typing import List


class Node:
    def __init__(self, index=None) -> None:
        self.index: int = index
        self.next: Node = None

    def add_front(self, node) -> None:
        node.next = self.next
        self.next = node


class Queue:
    def __init__(self, front: Node = None, rear: Node = None) -> None:
        self.front: Node = front
        self.rear: Node = rear
        self.count: int = 0

    def push(self, node: Node) -> None:
        if self.count == 0:
            self.front = node
        else:
            self.rear.next = node

        self.rear = node
        self.count += 1

    def pop(self) -> Node:
        if self.count == 0:
            print("Stack underflow occured!")
            return -999999

        node = self.front
        index = node.index

        self.front = node.next
        self.count -= 1

        return index


def bfs(graph: List[Node], check_list: list, start: int):
    q = Queue(None, None)

    node = Node(start)
    q.push(node)

    check_list[start] = 1

    while q.count != 0:
        x = q.pop()
        print(x, end=' ')

        curr: Node = graph[x].next

        while curr:
            next_index = curr.index

            if not check_list[next_index]:
                q.push(curr)
                check_list[next_index] = 1

            curr = curr.next
    print('', end='\n')


def main():
    graph: List[Node]
    check_list: List[int]

    n, m = map(int, input().split(' '))

    graph = [Node(i) for i in range(0, n+1)]
    check_list = [None for i in range(0, n+1)]

    for _ in range(m):
        x, y = map(int, input().split(' '))

        graph[x].add_front(Node(y))
        graph[y].add_front(Node(x))

    start = 1
    bfs(graph, check_list, start)


main()

# node: 5 line: 4

# 1 2
# 1 3
# 1 5
# 2 5

# result: 1 5 3 2
