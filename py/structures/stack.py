class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next = node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node()
        node.data = data
        node.next = self.top

        self.top = node

    def pop(self):
        if not self.top:
            print("스택 언더플로우가 발생했습니다. ")
            return None

        node = self.top
        data = node.data

        self.top = node.next

        return data

    def show(self):
        curr = self.top

        print("스택의 최상단 ")
        while curr:
            print(curr.data)
            curr = curr.next
        print("스택의 최하단 ")


def main():
    stack = Stack()
    stack.push(7)
    stack.push(5)
    stack.push(4)
    stack.pop()
    stack.push(6)
    stack.pop()
    stack.show()


main()
