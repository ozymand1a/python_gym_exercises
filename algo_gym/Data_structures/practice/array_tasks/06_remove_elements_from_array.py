from algo_gym.Data_structures.theory.array import Array


class ArrayWithRemoveElements(Array):
    def remove_elements(self, value):
        pass


if __name__ == '__main__':
    array = ArrayWithRemoveElements(5)
    array.append(6)
    array.append(2)
    array.append(1)
    array.append(2)
    array.append(9)
    print(array)
    array.remove_elements(2)
    print(array)
