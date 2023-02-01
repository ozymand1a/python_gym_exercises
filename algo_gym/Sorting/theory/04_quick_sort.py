def quick_sort(arr, start, end):

    # stop recursion
    if start >= end:
        return

    divider = arr[start]
    before, after = [], []
    i = start + 1
    while i < end + 1:
        if arr[i] < divider:
            before.append(arr[i])
        else:
            after.append(arr[i])
        i += 1

    index = start
    while len(before) > 0:
        arr[index] = before.pop()
        index += 1

    mid_point = index
    arr[index] = divider

    index += 1
    while len(after) > 0:
        arr[index] = after.pop()
        index += 1

    quick_sort(arr, start, mid_point - 1)
    quick_sort(arr, mid_point + 1, end)


if __name__ == '__main__':
    arr = [7, 8, 5, 9, 4, 1, 3]
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
