def clear_open_brackets_recursively(s, s_new, close_brackets, index):
    if index < 0:
        return s_new

    token = s[index]

    if token == ")":
        close_brackets += 1
        s_new = token + s_new
    elif token == "(":
        if close_brackets == 0:
            s_new = ""
        else:
            s_new = token + s_new
    else:
        s_new = token + s_new

    index -= 1

    return clear_open_brackets_recursively(s[:index + 1], s_new, close_brackets, index)


def clear_open_brackets(s):
    return clear_open_brackets_recursively(s, "", 0, len(s) - 1)


if __name__ == '__main__':
    print(clear_open_brackets("abcde((abc"))  # abcde
    print(clear_open_brackets("abcde((abcd)(abcd"))  # abcde((abcd)
