from algo_gym.Data_structures.theory.array import Array


class ArrayWithReverse(Array):
    def reverse(self):
        start, end = 0, self.length - 1
        print(end)

        while start < end:
            self.data[start], self.data[end] = self.data[end], self.data[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    array = ArrayWithReverse(5)
    array.append(6)
    array.append(2)
    array.append(1)
    array.append(9)
    array.append(4)
    print(array)
    array.reverse()
    print(array)
