class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.deleted = False

    def __str__(self):
        return f"[{self.key:03d}:{self.value}]"

    def delete(self):
        self.deleted = True
        self.key = None
        self.value = None


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
            if self.buckets[probe].key == key and not self.buckets[probe].deleted:
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
            if not self.buckets[probe] or self.buckets[probe].deleted:
                self.buckets[probe] = DataItem(key, value)
                self.num_elements += 1
                return

            if self.buckets[probe].key == key:
                raise ValueError(f"There is already element with key: {key}")

            probe = self._hash(probe + 1)

    def delete(self, key):
        item = self.get(key)
        if item:
            self.num_elements -= 1
            item.delete()

    def __str__(self):
        """
        Выводит все ячейки хэш-таблицы.
        """
        text = ""
        for i in range(self.size):
            if self.buckets[i] is None:
                text += f"{i: 3d}: [--------]\n"
            elif self.buckets[i].deleted:
                text += f"{i: 3d}: deleted\n"
            else:
                text += f"{i: 3d}: {self.buckets[i]}\n"

        return text


if __name__ == '__main__':
    ht = HashTableOpenAddressing(5)

    for key, value in map(
            lambda x: [int(x[1:4]), x],
            ["B617KM39RUS", "B398AB39RUS", "C254HE39RUS", "E123OK39RUS", "H637EA39RUS"]
    ):
        ht.insert(key, value)
    print(ht)
    ht.delete(617)
    ht.delete(637)
    print(ht)
    ht.insert(557, "H557OP39RUS")
    print(ht)
