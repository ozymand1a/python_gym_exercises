def gcd_iter(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_rec(a, b):
    if b:
        return gcd_rec(b, a % b)
    return a


if __name__ == '__main__':
    print(gcd_iter(4851, 3003))
    print(gcd_rec(4851, 3003))
