from algo_gym.Data_structures.theory.queue_from_array import QueueArrayBase


class QueueArray(QueueArrayBase):
    def __init__(self, size):
        QueueArrayBase.__init__(self, size=size)


if __name__ == '__main__':
    queue = QueueArray(4)
    queue.enqueue(12)
    queue.enqueue(7)
    queue.enqueue(6)
    print(queue)
