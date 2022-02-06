from algo_gym.Data_structures.theory.array import Array


class ArrayWithRemove(Array):
    def remove(self, value):
        for i in range(self.length):
            if self.data[i] == value:
                start = i
                end = self.length - 1

                while start < end:
                    self.data[start] = self.data[start + 1]
                    start += 1

                self.length -= 1
                break


if __name__ == '__main__':
    array = ArrayWithRemove(4)
    array.append(6)
    array.append(2)
    array.append(1)
    array.append(9)
    print(array)
    array.remove(6)
    print(array)
    array.remove(9)
    print(array)
