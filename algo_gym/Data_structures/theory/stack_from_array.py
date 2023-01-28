from algo_gym.Data_structures.theory.array import Array


class StackArrayBase(Array):
    def __init__(self, size):
        Array.__init__(self, size=size)
        self.top = -1

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        if self.length == 0:
            return None
        pop_element = self.data[self.top]
        self.length -= 1
        self.top -= 1

        return pop_element

    def push(self, value):
        """
        Push 'value' to stack
        """
        if self.length == self.size:
            raise OverflowError

        self.data[self.length] = value
        self.length += 1
        self.top += 1


if __name__ == '__main__':
    stack = StackArrayBase(3)
    stack.push(12)
    stack.push(7)
    stack.push(6)
    print(stack)
    # stack.push(8) # OverflowError
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
