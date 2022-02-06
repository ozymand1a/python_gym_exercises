def interpolation_search(arr, target):
    lo, hi = 0, len(arr) - 1
    steps = 0

    while lo <= hi:
        steps += 1

        # check equality
        if hi == lo:
            if arr[lo] == target:
                return lo, steps
            else:
                return -1, steps

        mid = lo + (hi - lo) * (target - arr[lo]) // (arr[hi] - arr[lo])

        if mid < lo or mid > hi:
            return -1, steps

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] > target:
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1

    return -1, steps


if __name__ == '__main__':
    arr = [2, 4, 7, 11, 12, 17, 23, 24, 26, 27, 29, 31, 33, 40, 43, 45, 46]
    print(interpolation_search(arr, 29))
    print(interpolation_search(arr, 43))
    print(interpolation_search(arr, 3))
    print(interpolation_search(arr, 22))
