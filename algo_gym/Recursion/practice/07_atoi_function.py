def atoi_function_recursively(s, number, index, num_iter):
    if index < 0:
        return number

    token = s[index]

    if token.isdigit():
        number = int(token) * 10 ** num_iter + number
    elif token == ".":
        number = number / 10 ** num_iter
        num_iter = -1
    elif token == "-":
        number = -number
    else:
        raise ValueError(f"There is no such symbol {token} at digit-like string!")

    num_iter += 1
    index -= 1

    return atoi_function_recursively(s[:index + 1], number, index, num_iter)


def atoi_function(s):
    # include negative and float numbers
    return atoi_function_recursively(s, 0, len(s) - 1, 0)


if __name__ == '__main__':
    print(f"string: 4159 with type: {type('4159')} "
          f"\nnumber: {atoi_function('4159')} with type: {type(atoi_function('4159'))}")
    print()
    print(f"string: -52.39 with type: {type('-52.39')} "
          f"\nnumber: {atoi_function('-52.39')} with type: {type(atoi_function('-52.39'))}")
