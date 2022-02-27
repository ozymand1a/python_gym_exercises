from algo_gym.Data_structures.practice.stack_tasks.stack_from_linked_list import StackLLBase


class StackLL(StackLLBase):
    def __init__(self):
        StackLLBase.__init__(self)


if __name__ == '__main__':
    stack = StackLL()
    stack.push(12)
    stack.push(7)
    stack.push(6)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.push(6)
    print(stack.pop())
    print(stack.pop())
