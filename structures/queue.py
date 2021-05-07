class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next = node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def push(self, data):
        node = Node()
        node.set_data(data)

        if self.count == 0:
            self.front = node
        else:
            self.rear.set_next(node)

        self.rear = node
        self.count += 1

    def pop(self):
        if self.count == 0:
            print("큐 언더 플로우가 발생했습니다. ")
            return None

        node = self.front
        data = node.data
        self.front = node.next
        self.count -= 1

        return data

    def show(self):
        curr = self.front

        print("큐의 가장 앞")

        while curr:
            print(curr.data)
            curr = curr.next

        print("큐의 가장 뒤")


def main():
    queue = Queue()

    queue.push(7)
    queue.push(5)
    queue.push(4)
    queue.pop()
    queue.push(6)
    queue.pop()

    queue.show()


main()
