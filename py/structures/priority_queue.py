MAX_SIZE = 1000000


class PriorityQueue:
    def __init__(self, heap=[], count=0):
        self.heap: list = heap
        self.count: int = count

    def log(self):
        [print(n, end=' ') for n in self.heap]

    def push(self, data: int):
        if self.count >= MAX_SIZE:
            return

        self.heap[self.count] = data

        now = self.count
        parent = int((self.count - 1) / 2)

        while now > 0 and self.heap[now] > self.heap[parent]:
            self.heap[now], self.heap[parent] = self.heap[parent], self.heap[now]
            now = parent
            parent = int((parent - 1) / 2)

        self.count += 1

    def pop(self):
        if self.count <= 0:
            return -9999

        res = self.heap[0]
        self.count -= 1

        self.heap[0] = self.heap[self.count]

        now = 0
        left_child = 1
        right_child = 2
        target = now

        while left_child < self.count:
            if self.heap[target] < self.heap[left_child]:
                target = left_child
            if self.heap[target] < self.heap[right_child] and right_child < self.count:
                target = right_child

            if target == now:
                break
            else:
                self.heap[now], self.heap[target]
                now = target
                left_child = now * 2 + 1
                right_child = now * 2 + 2

        return res


def main():
    n = int(input())

    heap = [None for _ in range(n)]
    pq = PriorityQueue(heap)

    for _ in range(n):
        data = int(input())
        pq.push(data)

    pq.log()

    print('\n')

    for _ in range(n):
        print(pq.pop())


main()
