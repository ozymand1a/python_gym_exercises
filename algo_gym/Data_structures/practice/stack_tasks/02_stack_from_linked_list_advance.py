from algo_gym.Data_structures.theory.linked_list import Node
from algo_gym.Data_structures.practice.stack_tasks.stack_from_linked_list import StackLLBase


class StackAdvance(StackLLBase):
    def __init__(self):
        StackLLBase.__init__(self)

    def peek(self):
        if self.top.next_node is not None:
            top_element = self.top.next_node.value
            return top_element

        return None

    def count(self):
        current = self.top.next_node
        len = 0

        while current is not None:
            current = current.next_node
            len += 1

        return len

    def clear(self):
        self.top = Node(None)


if __name__ == '__main__':
    stack = StackAdvance()
    stack.push(12)
    stack.push(7)
    stack.push(6)
    print(stack.peek())
    print(stack.count())
    stack.clear()
    print(stack.count())
    print(stack.peek())
