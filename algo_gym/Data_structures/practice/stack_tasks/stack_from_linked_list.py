from algo_gym.Data_structures.theory.linked_list import Node


class StackLLBase:
    def __init__(self):
        self.top = Node(None)

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        if self.top.next_node is not None:
            pop_element = self.top.next_node.value
            tail = self.top.next_node.next_node
            self.top.next_node = tail

            return pop_element

        return None

    def push(self, value):
        """
        Push 'value' to stack
        """
        tail = self.top.next_node
        self.top.next_node = Node(
            value=value,
            next_node=tail
        )
