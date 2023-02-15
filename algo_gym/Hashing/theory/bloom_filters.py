import math
import mmh3
from bitarray import bitarray


class BloomFilter:
    def __init__(self, items_count, fp_prob):
        self.fp_prob = fp_prob

        # calc bloom filter params
        self.size = BloomFilter.get_size(items_count, fp_prob)
        self.hash_count = BloomFilter.get_hash_count(self.size, items_count)

        # Init bit array
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size

            self.bit_array[index] = 1

    def check(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size

            if not self.bit_array[index]:
                return False

        return True

    @staticmethod
    def get_size(n, p):
        m = - (n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @staticmethod
    def get_hash_count(m, n):
        k = (m * math.log(2)) / n
        return int(k)

    def __str__(self):
        return self.bit_array.to01()


if __name__ == '__main__':
    bloom_filter = BloomFilter(20, 0.1)

    bloom_filter.add("973")
    bloom_filter.add("497")

    print(bloom_filter.check("973"))  # True
    print(bloom_filter.check("497"))  # True
    print(bloom_filter.check("124"))  # False
    print(bloom_filter.check("26196"))  # True
