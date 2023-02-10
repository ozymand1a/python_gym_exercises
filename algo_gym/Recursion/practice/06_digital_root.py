def digital_root_recursive(number, root):
    if not number:
        return root

    root += number % 10
    root_sub = 0
    while root:
        root_sub += root % 10
        root //= 10
    root = root_sub
    number //= 10

    return digital_root_recursive(number, root)


def digital_root(number):
    return digital_root_recursive(number, root=0)


if __name__ == '__main__':
    print(digital_root(9999999))  # 63 -> 9
    print(digital_root(1000))  # 1 -> 1
    print(digital_root(4444))  # 16 -> 7
