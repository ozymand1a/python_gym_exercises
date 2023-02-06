def sieve_eratosthenes(n):
    storage = [True] * (n + 1)
    result = []
    # initial value
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


if __name__ == '__main__':
    print(sieve_eratosthenes(30))
