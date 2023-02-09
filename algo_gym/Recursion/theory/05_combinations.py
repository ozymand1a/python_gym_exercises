from itertools import combinations as i_combinations


def combinations(elements, k):
    if k == 0:
        return [[]]

    result = []
    i = 0
    while i < len(elements):
        element = elements[i]
        combs = combinations(elements[i + 1:], k - 1)
        print(combs)

        # iteratively add suffix to base element
        for suffix in combs:
            result.append([element] + suffix)
        i += 1

    return result


if __name__ == '__main__':
    print(combinations(["A", "B", "C", "D"], 3))
    print(list(i_combinations(["A", "B", "C", "D"], 3)))
