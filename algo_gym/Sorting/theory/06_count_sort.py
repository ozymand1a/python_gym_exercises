def count_sort(arr, n):
    count_storage = [0 for i in range(n + 1)]

    for i in range(len(arr)):
        count_storage[arr[i]] += 1

    j = 0
    for i in range(len(count_storage)):
        for _ in range(count_storage[i]):
            arr[j] = i
            j += 1


if __name__ == '__main__':
    arr = [7, 8, 5, 9, 4, 1, 3]
    print(arr)
    count_sort(arr, max(arr))
    print(arr)
