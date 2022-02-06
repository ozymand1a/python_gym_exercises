def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1

    return -1


if __name__ == '__main__':
    arr = [1, 2, 4, 7, 8, 12, 15, 20]
    print(binary_search(arr, 15))
    print(binary_search(arr, 3))
