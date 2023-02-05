from algo_gym.Data_structures.theory.stack_from_array_doubly import DoublyStackArray


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
