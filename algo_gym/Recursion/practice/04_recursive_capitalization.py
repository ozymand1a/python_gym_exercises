def capitalization(money, percent, num_month):
    if num_month == 0:
        return money

    money += money * percent / (12 * 100)

    return int(capitalization(money, percent, num_month - 1))


if __name__ == '__main__':
    money_update = capitalization(10000, 10, 2)
    print(money_update)
