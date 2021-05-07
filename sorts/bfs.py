from collections import deque
from queue import Queue

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
# 한 노드를 중심으로 연결 관계가 있는 노드를 모두 표현해준다


def bfs(graph, root):
    visited = []
    queue = Queue()

    queue.put(root)

    while not queue.empty():
        node = queue.get()

        if node not in visited:
            visited.append(node)

            for next_node in graph[node]:
                queue.put(next_node)

    print(visited)
    return visited


def bfs_recursive(graph, queue: Queue, path):
    if not queue:
        return

    node = queue.get()
    
    


if __name__ == "__main__":
    bfs(graph, 'A')
