def sum_num(n):
    if n == 1:
        return 1

    return n + sum_num(n - 1)


if __name__ == '__main__':
    res = sum_num(5)
    print(res)
