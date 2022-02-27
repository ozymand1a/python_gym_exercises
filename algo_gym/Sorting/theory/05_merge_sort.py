def merge_sort(arr):
    temp_arr = [None] * len(arr)
    do_merge(arr, temp_arr, 0, len(arr) - 1)


def do_merge(arr, temp_arr, start, end):

    if start == end:
        return

    # middle index at array
    midpoint = (start + end) // 2

    do_merge(arr, temp_arr, start, midpoint)
    do_merge(arr, temp_arr, midpoint + 1, end)

    # merge arrays
    left_index = start
    right_index = midpoint + 1
    temp_arr_index = left_index
    while left_index <= midpoint and right_index <= end:
        if arr[left_index] <= arr[right_index]:
            temp_arr[temp_arr_index] = arr[left_index]
            left_index += 1
        else:
            temp_arr[temp_arr_index] = arr[right_index]
            right_index += 1
        temp_arr_index += 1

    for i in range(left_index, midpoint + 1):
        temp_arr[temp_arr_index] = arr[i]
        temp_arr_index += 1
    for i in range(right_index, end + 1):
        temp_arr[temp_arr_index] = arr[i]
        temp_arr_index += 1

    for i in range(start, end + 1):
        arr[i] = temp_arr[i]


if __name__ == '__main__':
    arr = [7, 8, 5, 9, 4, 1]
    print(arr)
    merge_sort(arr)
    print(arr)
