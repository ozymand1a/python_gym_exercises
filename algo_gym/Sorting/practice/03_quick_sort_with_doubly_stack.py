from algo_gym.Data_structures.theory.stack_from_array_doubly import DoublyStackArray


def do_quick_sort_with_doubly_stack(arr, stack, start, end):
    # break recursion
    if start >= end:
        return

    # push elements from arr to stack
    divider = arr[start]
    index = start + 1
    while index <= end:
        if arr[index] <= divider:
            stack.push_left(arr[index])
        else:
            stack.push_right(arr[index])
        index += 1

    index = start
    while not stack.is_left_empty():
        arr[index] = stack.pop_left()
        index += 1

    mid_point = index
    arr[mid_point] = divider

    index += 1
    while not stack.is_right_empty():
        arr[index] = stack.pop_right()
        index += 1

    do_quick_sort_with_doubly_stack(arr, stack, start, mid_point - 1)
    do_quick_sort_with_doubly_stack(arr, stack, mid_point + 1, end)


def quick_sort_with_doubly_stack(arr):
    stack = DoublyStackArray(len(arr))
    do_quick_sort_with_doubly_stack(arr, stack, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [7, 8, 5, 9, 4, 1, 3]
    print(arr)
    quick_sort_with_doubly_stack(arr)
    print(arr)
