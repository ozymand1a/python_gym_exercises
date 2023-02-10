def count_units(number):
    if not number:
        return 0

    num_units = 0
    if number % 2 == 1:
        num_units += 1

    number //= 2

    return num_units + count_units(number)


if __name__ == '__main__':
    print(count_units(7145))  # 1101111101001
    print(count_units(237))  # 11101101
