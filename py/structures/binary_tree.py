class Node:
    def __init__(self, data, leftChild, rightChild):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild


def init_node(data, leftChild, rightChild):
    return Node(data, leftChild, rightChild)


def pre_order(root):
    if root:
        print(root.data, end=' ')
        pre_order(root.leftChild)
        pre_order(root.rightChild)


def in_order(root):
    if root:
        in_order(root.leftChild)
        print(root.data, end=' ')
        in_order(root.rightChild)


def post_order(root):
    if root:
        post_order(root.leftChild)
        post_order(root.rightChild)
        print(root.data, end=' ')


def main():
    n7 = init_node(50, None, None)
    n6 = init_node(37, None, None)
    n5 = init_node(23, None, None)
    n4 = init_node(5, None, None)
    n3 = init_node(48, n6, n7)
    n2 = init_node(17, n4, n5)
    n1 = init_node(30, n2, n3)

    pre_order(n1)
    print('\n')

    in_order(n1)
    print('\n')

    post_order(n1)
    print('\n')


main()

# 30 17 5 23 48 37 50
# 5 17 23 30 37 48 50
# 5 23 17 37 50 48 30
