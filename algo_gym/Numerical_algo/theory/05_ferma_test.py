from random import randint


def ferma_test(p, tests):
    """
    Is this number prime?
    """
    for i in range(tests):
        a = randint(1, p)

        if pow(a, p - 1, p) != 1:
            return False

    return True


if __name__ == '__main__':
    tests = 10

    # Простые числа
    print(3539, ferma_test(3539, tests))
    print(479001599, ferma_test(479001599, tests))

    # Составные числа
    print(2856, ferma_test(2856, tests))
    print(3537, ferma_test(3537, tests))

    # Число Кармайкла (составное)
    print(321197185, ferma_test(321197185, tests))
