import math
from algo_gym.Data_structures.theory.array import Array


class ArrayWithStats(Array):
    def min(self):
        if self.length == 0:
            return None
        else:
            min_value = math.inf
            for i in range(self.length):
                min_value = min(min_value, self.data[i])

            return min_value

    def max(self):
        if self.length == 0:
            return None
        else:
            max_value = -math.inf
            for i in range(self.length):
                max_value = max(max_value, self.data[i])

            return max_value

    def avg(self):
        if self.length == 0:
            return None
        else:
            sum_value = 0
            for i in range(self.length):
                sum_value += self.data[i]

            return sum_value / self.length


if __name__ == '__main__':
    array = ArrayWithStats(4)
    array.append(6)
    array.append(2)
    array.append(1)
    array.append(9)
    print(array.min())
    print(array.max())
    print(array.avg())
