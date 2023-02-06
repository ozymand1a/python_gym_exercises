def exp(value, p):
    result = 1

    factor = value

    while p:
        if p % 2 == 1:
            result *= factor

        factor *= factor
        p //= 2

    return result


if __name__ == '__main__':
    print(exp(2, 11))
