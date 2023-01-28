from algo_gym.Data_structures.theory.stack_from_array import StackArrayBase


class StackArray(StackArrayBase):
    def __init__(self, size):
        StackArrayBase.__init__(self, size=size)


if __name__ == '__main__':
    stack = StackArray(3)
    stack.push(12)
    stack.push(7)
    stack.push(6)
    print(stack)
    # stack.push(8) # OverflowError
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
