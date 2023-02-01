import random


def count_sort_with_negative_numbers(arr):
    max_value, min_value = float("-inf"), float("inf")

    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
        if arr[i] < min_value:
            min_value = arr[i]

    count_storage_positive = [0] * (max_value + 1)
    count_storage_negative = [0] * (abs(min_value) + 1)

    for i in range(len(arr)):
        if arr[i] >= 0:
            count_storage_positive[arr[i]] += 1
        else:
            count_storage_negative[abs(arr[i])] += 1

    j = 0
    for i in reversed(range(len(count_storage_negative))):
        for _ in range(count_storage_negative[i]):
            arr[j] = -i
            j += 1

    for i in range(len(count_storage_positive)):
        for _ in range(count_storage_positive[i]):
            arr[j] = i
            j += 1


if __name__ == '__main__':
    arr = [random.randrange(-2, 3) for i in range(15)]
    print(arr)
    count_sort_with_negative_numbers(arr)
    print(arr)
