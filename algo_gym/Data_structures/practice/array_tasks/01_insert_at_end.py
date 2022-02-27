from algo_gym.Data_structures.theory.array import Array


class ArrayWithAppend(Array):
    def __init__(self, size):
        Array.__init__(self, size)


if __name__ == '__main__':
    array = ArrayWithAppend(3)
    print(array.size)
    print(array.length)
    print(array)
    array.append(20)
    array.append(10)
    array.append(30)
    print(array)
    array.append(40)
