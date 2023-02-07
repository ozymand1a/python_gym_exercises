def find_prime_factors(number):
    """
    This algo has exponential complexity
    """
    factors = []

    # make number odd
    while number % 2 == 0:
        factors.append(2)
        number //= 2

    i = 3
    max_factor = number ** 0.5
    while i <= max_factor:
        while number % i == 0:
            factors.append(i)
            number //= i
            max_factor = number ** 0.5

        # only odd numbers
        i += 2

    if number > 1:
        factors.append(number)

    return factors


if __name__ == '__main__':
    print(23 * 17, find_prime_factors(23 * 17))
    print(137 * 239, find_prime_factors(137 * 239))
    print(1046527 * 16127, find_prime_factors(1046527 * 16127))
    print(16769023 * 1073676287, find_prime_factors(16769023 * 1073676287))

    # Составное число.
    print(545632, find_prime_factors(545632))
