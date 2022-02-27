from algo_gym.Data_structures.theory.array import Array


class ArrayWithInsert(Array):
    def insert(self, idx, value):

        if self.length == self.size:
            raise OverflowError
        elif idx > self.length:
            self.data[self.length] = value
            self.length += 1
        else:
            start = idx
            end = self.length - 1

            while start <= end:
                self.data[end + 1] = self.data[end]
                end -= 1
            self.data[idx] = value
            self.length += 1


if __name__ == '__main__':
    array = ArrayWithInsert(5)
    array.append(20)
    array.append(10)
    array.append(30)
    array.insert(1, 40)  # вставка на позицию 1
    print(array)
    array.insert(20, 50)  # Индекс за пределами массива.
    print(array)
    array.insert(2, 50)  # Переполнение.
