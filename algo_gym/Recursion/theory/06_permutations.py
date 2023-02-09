from itertools import permutations as i_permutations


def permutations(elements, k):
    if k == 0:
        return [[]]

    result = []
    i = 0
    while i < len(elements):
        element = elements[i]

        # order is not important now
        new_elements = elements[:]
        new_elements.remove(element)
        perms = permutations(new_elements, k - 1)

        for suffix in perms:
            result.append([element] + suffix)
        i += 1

    return result


if __name__ == '__main__':
    print(permutations(["A", "B", "C", "D"], 3))
    print(list(i_permutations(["A", "B", "C", "D"], 3)))
