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


def dfs_recursive(graph, root, visited=[]):
    visited.append(root)

    for node in graph:
        if node not in visited:
            visitied = dfs_recursive(graph, node, visited)

    return visited


def dfs(graph, root_node):
    path = []
    stack = []

    stack.append(root_node)

    while stack:
        node = stack.pop()

        if node not in path:
            path.append(node)

            next_nodes = graph[node]
            stack.extend(reversed(next_nodes))

    print(path)
    return path


def dfs_recursive(graph, root_node, path=[]):
    path.append(root_node)

    for node in graph:
        if node not in path:
            path = dfs_recursive(graph, node, path)

    return path


if __name__ == "__main__":
    dfs(graph, "A")
    path = dfs_recursive(graph, "A")
    print(path)
