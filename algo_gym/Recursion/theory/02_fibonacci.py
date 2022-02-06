fibs = [None] * 100


def fibonacci(n):
    if fibs[n] is not None:
        return fibs[n]

    if n <= 1:
        return n

    fibs[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibs[n]


if __name__ == '__main__':
    for i in range(10):
        print(fibonacci(i), end=' ')
