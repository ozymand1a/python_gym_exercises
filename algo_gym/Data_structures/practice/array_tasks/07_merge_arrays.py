def merge(array1, array2):
    """
    Функция слияния двух отсортированных массивов в один.
    array1 и array2 - массивы представленные python-списками.
    """
    i, j = 0, 0
    n, m = len(array1) - 1, len(array2) - 1
    result = [None] * (n + m + 2)
    result_idx = 0

    while i <= n and j <= m:
        if array1[i] <= array2[j]:
            result[result_idx] = array1[i]
            i += 1
        else:
            result[result_idx] = array2[j]
            j += 1
        result_idx += 1

    while i <= n:
        result[result_idx] = array1[i]
        result_idx += 1
        i += 1

    while j <= m:
        result[result_idx] = array2[j]
        result_idx += 1
        j += 1

    return result


if __name__ == '__main__':
    array1 = [3, 4, 7, 8]
    array2 = [1, 5, 9]
    array = merge(array1, array2)
    print(array)
