class DoublyStackArray:
    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size
        # Длина заполнненого массива.
        self.length = 0
        # Полный размер массива.
        self.size = size

        self.pointer_left = -1
        self.pointer_right = self.size

    def push_left(self, value):
        if self.length == self.size:
            raise OverflowError

        self.pointer_left += 1
        self.data[self.pointer_left] = value
        self.length += 1

    def push_right(self, value):
        if self.length == self.size:
            raise OverflowError

        self.pointer_right -= 1
        self.data[self.pointer_right] = value
        self.length += 1

    def pop_left(self):
        if self.pointer_left == -1:
            return None

        pop_element = self.data[self.pointer_left]
        self.data[self.pointer_left] = None
        self.length -= 1
        self.pointer_left -= 1
        return pop_element

    def pop_right(self):
        if self.pointer_right == self.size:
            return None

        pop_element = self.data[self.pointer_right]
        self.data[self.pointer_right] = None
        self.length -= 1
        self.pointer_right += 1
        return pop_element

    def clear(self):
        self.data = [None] * self.size
        self.length = 0

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data)) + "]"


if __name__ == '__main__':
    stack = DoublyStackArray(5)
    stack.push_left(12)
    stack.push_left(7)
    stack.push_left(6)
    stack.push_right(8)
    # stack.push_left(3)  # Overflow Error
    print(stack)
    print(stack.pop_left())
    print(stack.pop_right())
    print(stack.pop_right())
    print(stack)
