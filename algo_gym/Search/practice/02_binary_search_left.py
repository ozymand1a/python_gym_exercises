def binary_search_left(arr, target):
    lo, hi = 0, len(arr) - 1
    ans = -1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            ans = mid
            hi = mid - 1
        elif arr[mid] > target:
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1

    return ans


if __name__ == '__main__':
    print(binary_search_left([1, 1, 2, 2, 2, 3, 4, 8], 2))  # 2 because it is the first occurrence of "2"
    print(binary_search_left([1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 8], 2))  # 1 because it is the first occurrence of "2"
