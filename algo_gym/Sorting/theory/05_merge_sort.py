def merge_sort(arr):
    temp_arr = [None] * len(arr)

    do_mergesort(arr, temp_arr, 0, len(arr) - 1)


def do_mergesort(arr, temp_arr, start, end):

    # stop recursion
    if start == end:
        return

    mid_point = (start + end) // 2
    do_mergesort(arr, temp_arr, start, mid_point)
    do_mergesort(arr, temp_arr, mid_point + 1, end)

    left_index = start
    right_index = mid_point + 1
    temp_arr_index = left_index
    while (left_index <= mid_point) and (right_index <= end):
        if arr[left_index] < arr[right_index]:
            temp_arr[temp_arr_index] = arr[left_index]
            left_index += 1
        else:
            temp_arr[temp_arr_index] = arr[right_index]
            right_index += 1
        temp_arr_index += 1

    while left_index <= mid_point:
        temp_arr[temp_arr_index] = arr[left_index]
        left_index += 1
        temp_arr_index += 1

    while right_index <= end:
        temp_arr[temp_arr_index] = arr[right_index]
        right_index += 1
        temp_arr_index += 1

    for i in range(start, end + 1):
        arr[i] = temp_arr[i]


if __name__ == '__main__':
    arr = [7, 8, 5, 9, 4, 1]
    print(arr)
    merge_sort(arr)
    print(arr)
