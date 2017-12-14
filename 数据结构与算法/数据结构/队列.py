# 队列（queue）只允许在一端进行插入操作，而在另一端进行删除操作，按照先进先出的的原理运作


class Queue(object):
    def __init__(self):
        self.list = []

    def enqueue(self,item):
        self.list.append(item)

    def dequeue(self):
        return self.list.pop(0)

    def is_empty(self):
        return len(self.list) is 0

    def size(self):
        return len(self.list)


queue = Queue()
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())






















