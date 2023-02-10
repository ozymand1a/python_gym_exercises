def digits_sum(value):
    if not value:
        return 0

    number = value % 10
    value //= 10

    return number + digits_sum(value)


if __name__ == '__main__':
    print(digits_sum(1532))
