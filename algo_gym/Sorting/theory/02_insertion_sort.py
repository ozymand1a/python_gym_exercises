def insertion_sort(arr):
    start = 0
    while start < len(arr) - 1:
        i = start + 1
        while arr[i] < arr[i - 1] and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
        start += 1


if __name__ == '__main__':
    arr = [7, 8, 5, 9, 4, 1, 3]
    print(arr)
    insertion_sort(arr)
    print(arr)
