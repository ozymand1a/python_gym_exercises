from functools import reduce


def sieve_eratosthenes(n):
    storage = [True] * (n + 1)
    result = []
    p = 2

    while p <= n:
        if storage[p]:
            result.append(p)

            factor = 2
            p_mult = p * factor
            while p_mult <= n:
                storage[p_mult] = False
                factor += 1
                p_mult = p * factor

        p += 1

    return result


def primorial(n):
    p_numbers = sieve_eratosthenes(n)
    return reduce(lambda a, b: a * b, p_numbers)


if __name__ == '__main__':
    print(primorial(13))  # 30 030
