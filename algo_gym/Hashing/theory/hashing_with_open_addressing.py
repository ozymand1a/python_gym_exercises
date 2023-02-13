class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"[{self.key:03d}:{self.value}]"


class HashTableOpenAddressing:
    def __init__(self, size):
        self.size = size
        self.num_elements = 0

        self.buckets = [None for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def get(self, key):
        """
        return element by key
        """
        probe = self._hash(key)
        num_probes = 0

        while True:
            num_probes += 1

            if not self.buckets[probe]:
                return None
            if self.buckets[probe].key == key:
                return self.buckets[probe]
            if num_probes == self.size:
                return None

            probe = self._hash(probe + 1)

    def insert(self, key, value):
        """
        insert at top Linked List
        """
        if self.num_elements == self.size:
            raise OverflowError

        probe = self._hash(key)

        while True:
            if not self.buckets[probe]:
                self.buckets[probe] = DataItem(key, value)
                self.num_elements += 1
                return

            if self.buckets[probe].key == key:
                raise ValueError(f"There is already element with key: {key}")

            probe = self._hash(probe + 1)

    def delete(self, key):
        pass

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
    ht = HashTableOpenAddressing(20)

    for key, value in map(lambda x: [int(x[1:4]), x],
                          ["B617KM39RUS", "B313AB39RUS", "C254HE39RUS", "E123OK39RUS",
                           "H637EA39RUS", "O129BA39RUS", "T765KP39RUS", "E389BT39RUS",
                           "B204BA39RUS", "M001EC39RUS", "A973AA39RUS", "C349EP39RUS",
                           "C166OK39RUS", "H555HH39RUS", "K675KH39RUS", "E746OP39RUS",
                           "T162BA39RUS", "C130BE39RUS", "B498BE39RUS", "B516MK39RUS"]):
        ht.insert(key, value)

    print(ht)

    print(ht.get(617))  # [617:B617KM39RUS]
    print(ht.get(134))  # None
