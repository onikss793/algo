class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next = node


class Linked_list:
    def __init__(self):
        self.head = Node()

    def add_front(self, data):
        node = Node()
        node.set_data(data)
        node.set_next(self.head.next)
        self.head.set_next(node)

    def remove_front(self):
        node = self.head.next
        self.head.next = node.next

    def show(self):
        curr = self.head.next

        while curr:
            print(curr.data)
            curr = curr.next


def main():
    linked_list = Linked_list()

    linked_list.add_front(2)
    linked_list.add_front(1)
    linked_list.add_front(7)
    linked_list.add_front(8)
    linked_list.remove_front()

    linked_list.show()


main()
