from algo_gym.Data_structures.theory.queue_from_linked_list import QueueDLLBase


class QueueDLL(QueueDLLBase):
    def __init__(self):
        QueueDLLBase.__init__(self)


if __name__ == '__main__':
    queue = QueueDLL()
    queue.enqueue(12)
    queue.enqueue(7)
    queue.enqueue(6)
    print(queue, queue.first)
