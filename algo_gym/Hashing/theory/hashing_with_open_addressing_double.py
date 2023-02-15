class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"[{self.key:03d}:{self.value}]"


class HashTableOpenAddressingDouble:
    PRIME = 7

    def __init__(self, size):
        self.size = size
        self.num_elements = 0

        self.buckets = [None for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def _hash_2(self, key):
        return HashTableOpenAddressingDouble.PRIME - (key % HashTableOpenAddressingDouble.PRIME)

    def get(self, key):
        num_probes = 0

        while True:
            num_probes += 1

            # index for insert
            probe = (self._hash(key) + num_probes * self._hash_2(key)) % self.size

            if not self.buckets[probe]:
                return None

            if self.buckets[probe].key == key:
                return self.buckets[probe]

            if num_probes == self.size:
                return None

    def insert(self, key, value):
        if self.num_elements == self.size:
            raise OverflowError

        step = 0
        while True:
            step += 1

            probe = (self._hash(key) + step * self._hash_2(key)) % self.size

            if not self.buckets[probe]:
                self.buckets[probe] = DataItem(key, value)
                self.num_elements += 1
                return

            if step == self.size:
                return

            if self.buckets[probe].key == key:
                raise ValueError(f"There is already element with key: {key}")

    def __str__(self):
        """
        Выводит все ячейки хэш-таблицы.
        """
        text = ""
        for i in range(self.size):
            if self.buckets[i] is None:
                text += f"{i: 3d}: [--------]\n"
            else:
                text += f"{i: 3d}: {self.buckets[i]}\n"

        return text


if __name__ == '__main__':
    ht = HashTableOpenAddressingDouble(20)

    for key, value in map(lambda x: [int(x[1:4]), x],
                          ["B617KM39RUS", "B313AB39RUS", "C254HE39RUS", "E123OK39RUS",
                           "H637EA39RUS", "O129BA39RUS", "T765KP39RUS", "E389BT39RUS",
                           "B204BA39RUS", "M001EC39RUS", "A973AA39RUS", "C349EP39RUS",
                           "C166OK39RUS", "H555HH39RUS", "K675KH39RUS", "E746OP39RUS",
                           "T162BA39RUS", "C130BE39RUS", "B498BE39RUS", "B516MK39RUS"]):
        ht.insert(key, value)

    print(ht)
    print(ht.get(555))  # [555:H555HH39RUS]
