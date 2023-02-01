def bubble_sort_reverse(arr):
    is_sorted = False
    n = 1

    while not is_sorted:
        is_sorted = True

        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
                is_sorted = False

        n += 1


if __name__ == '__main__':
    arr = [7, 8, 5, 9, 4, 1]
    print(arr)
    bubble_sort_reverse(arr)
    print(arr)
