from algo_gym.Data_structures.theory.stack_from_array import StackArrayBase


class StackArrayAdvance(StackArrayBase):
    def __init__(self, size):
        StackArrayBase.__init__(self, size=size)

    def peek(self):
        return self.data[self.top] if self.length != 0 else None

    def count(self):
        return self.length

    def clear(self):
        self.data = [None] * self.size
        self.length = 0


if __name__ == '__main__':
    stack = StackArrayAdvance(3)
    stack.push(12)
    stack.push(7)
    stack.push(6)
    print(stack.peek())
    print(stack.count())
    stack.clear()
    print(stack.count())
    print(stack.peek())
