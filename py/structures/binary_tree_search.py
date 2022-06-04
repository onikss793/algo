class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left_child: Node = None
        self.right_child: Node = None


def insert_node(root: Node, data: int):
    if not root:
        return Node(data)

    if root.data > data:
        root.left_child = insert_node(root.left_child, data)
    else:
        root.right_child = insert_node(root.right_child, data)

    return root


def search_node(root: Node, data: int) -> Node:
    if not root:
        return None
    if root.data == data:
        return root
    elif root.data > data:
        return search_node(root.left_child, data)
    else:
        return search_node(root.right_child, data)


def pre_order(root: Node) -> None:
    if not root:
        return

    print(root.data, end=' ')

    pre_order(root.left_child)
    pre_order(root.right_child)


def find_min_node(root: Node) -> Node:
    node = root

    while not node and node.left_child:
        node = node.left_child

    return node


def delete_node(root: Node, data: int) -> Node:
    if not root:
        return None

    node: Node

    if root.data > data:
        root.left_child = delete_node(root.left_child, data)
    elif root.data < data:
        root.right_child = delete_node(root.right_child, data)
    else:
        if root.left_child and root.right_child:
            node = find_min_node(root.right_child)
            root.data = node.data
            root.right_child = delete_node(root.right_child, node.data)
        else:
            return root.left_child if not root.left_child else root.right_child

    return root


def main():
    root = insert_node(None, 30)
    insert_node(root, 17)
    insert_node(root, 48)
    insert_node(root, 5)
    insert_node(root, 23)
    insert_node(root, 37)
    insert_node(root, 50)

    pre_order(root)
    print('', end='\n')

    delete_node(root, 30)

    pre_order(root)
    print('', end='\n')


if __name__ == '__main__':
    main()
