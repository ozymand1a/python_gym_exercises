def primal_test(n):
    n_sqrt = int(n ** 0.5)
    for i in range(2, n_sqrt + 1):
        if n % i == 0:
            return "not_prime"

    return "prime"


if __name__ == '__main__':
    print(primal_test(2243))  # "prime"
    print(primal_test(1293))  # "not_prime"
