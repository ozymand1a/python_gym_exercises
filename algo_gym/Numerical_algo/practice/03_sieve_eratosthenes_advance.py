def sieve_eratosthenes_advance(n):
    """
    remove even numbers from filtering
    """
    storage = [True if i % 2 != 0 else False for i in range(n + 1)]
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


if __name__ == '__main__':
    print(sieve_eratosthenes_advance(30))
