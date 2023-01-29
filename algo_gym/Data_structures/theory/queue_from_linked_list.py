from algo_gym.Data_structures.theory.linked_list_doubly import NodeDoubly, ListDoubly


class QueueDLLBase(ListDoubly):
    def __init__(self):
        ListDoubly.__init__(self)
        self.first = None

    def enqueue(self, value):
        """
        Добавляет элемент со значением value в очередь.
        """
        current = self.top
        next_node = current.next_node

        if self.first is None:
            self.first = NodeDoubly(value)
            self.first.prev_node = current
            self.first.next_node = next_node
            current.next_node = self.first
        else:
            new_node = NodeDoubly(value)
            # new_node connections from inner
            new_node.next_node = next_node
            new_node.prev_node = current
            # new node connections from outer
            current.next_node = new_node
            next_node.prev_node = new_node

    def dequeue(self):
        """
        Извлекает элемент из очереди.
        """
        if self.top.next_node is None:
            return None

        dequeue_element = self.first.value
        prev_node = self.first.prev_node
        next_node = self.first.next_node
        # reassign
        prev_node.next_node = next_node
        self.first = prev_node

        return dequeue_element


if __name__ == '__main__':
    queue = QueueDLLBase()
    queue.enqueue(15)
    queue.enqueue(17)
    queue.enqueue(39)
    queue.enqueue(24)
    print(queue, queue.first)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue, queue.first)
    queue.enqueue(15)
    queue.enqueue(17)
    print(queue, queue.first)
