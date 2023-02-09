def digits_sum(value):
    if value % 10 == value:
        return value

    return int(str(value)[0]) + digits_sum(int(str(value)[1:]))


if __name__ == '__main__':
    res = digits_sum(1531)
    print(res)
