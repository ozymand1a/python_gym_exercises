from algo_gym.Data_structures.theory.array import Array


class ArrayWithRemoveElements(Array):
    def remove_elements(self, value):
        start = 0
        end = self.length
        for j in range(end):
            if self.data[j] != value:
                self.data[start] = self.data[j]
                start += 1
            else:
                self.length -= 1


if __name__ == '__main__':
    array = ArrayWithRemoveElements(9)
    array.append(6)
    array.append(2)
    array.append(1)
    array.append(2)
    array.append(2)
    array.append(8)
    array.append(2)
    array.append(3)
    array.append(9)
    print(array)
    array.remove_elements(2)
    print(array)
