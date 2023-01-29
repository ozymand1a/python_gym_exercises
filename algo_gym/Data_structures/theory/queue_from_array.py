from algo_gym.Data_structures.theory.array import Array


class QueueArrayBase(Array):
    def __init__(self, size):
        Array.__init__(self, size=size)
        self.first = -1
        self.last = -1

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        if self.size == self.length:
            raise OverflowError

        if self.first == -1:
            self.first = 0
        self.last = (self.last + 1) % self.size
        self.data[self.last] = value
        self.length += 1

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        if self.length == 0:
            return None

        dequeue_element = self.data[self.first]
        self.data[self.first] = None
        self.first = (self.first + 1) % self.size
        self.length -= 1

        return dequeue_element

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data)) + "]"


if __name__ == '__main__':
    queue = QueueArrayBase(6)
    queue.enqueue(15)
    queue.enqueue(17)
    queue.enqueue(39)
    queue.enqueue(24)
    print(queue)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)
    queue.enqueue(15)
    queue.enqueue(17)
    print(queue)
    queue.enqueue(77)
    print(queue)
    print(f"first: {queue.first} and last: {queue.last}")
