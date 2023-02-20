def binary_search_right(arr, target):
    lo, hi = 0, len(arr) - 1
    ans = -1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            lo = mid + 1
            ans = mid
        elif arr[mid] > target:
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1

    return ans


if __name__ == '__main__':
    print(binary_search_right([1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 8], 2))  # 3 because it is the last occurrence of "2"
