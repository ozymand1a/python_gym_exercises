from algo_gym.Data_structures.theory.queue_from_linked_list import QueueDLLBase


class QueueDLLAdvance(QueueDLLBase):
    def __init__(self):
        QueueDLLBase.__init__(self)

    def peek(self):
        return self.first.value if self.first else None

    def count(self):
        length = 0
        current = self.top

        while current.next_node:
            current = current.next_node
            length += 1

        return length

    def clear(self):
        self.top.next_node = None
        self.first = None


if __name__ == '__main__':
    queue = QueueDLLAdvance()
    queue.enqueue(12)
    queue.enqueue(7)
    queue.enqueue(6)
    print(queue)
    print(queue.dequeue())
    print(queue.count())
    print(queue.peek())
    queue.clear()
    print(queue)
