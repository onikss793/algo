from typing import List


class Node:
    def __init__(self, index, next):
        self.index: int = index
        self.next: Node = next


def add_front(root: Node, index: int):
    node = Node(index, root.next)
    root.next = node


def show_all(root: Node):
    curr = root

    while curr:
        print(
            f"{curr.index} -> {curr.next.index if curr.next else None}",
            end=' '
        )
        curr = curr.next
    print('', end='\n')


def dfs(index: int, graph: List[Node], stack: List[bool]):
    if stack[index]:
        return

    stack[index] = True
    print(f"{index} 조회했음")

    next_node = graph[index]

    while next_node:
        dfs(next_node.index, graph, stack)
        next_node = next_node.next


def main():
    n, m = map(int, input().split())
    graph = [Node(i, None) for i in range(n+1)]
    stack = [False]*(n+1)

    for _ in range(m):
        x, y = map(int, input().split())
        add_front(graph[x], y)
        add_front(graph[y], x)

    [show_all(node) for node in graph]

    dfs(3, graph, stack)


main()
