from algo_gym.Hashing.theory.hashing_with_separate_chaining import Cell, HashTableSeparateChaining


class HashTableSeparateChainingWithUpdate(HashTableSeparateChaining):
    def __init__(self, size):
        HashTableSeparateChaining.__init__(self, size=size)

    def insert(self, key, value):
        if self.get(key) is not None:
            cell_before = self._find_cell_before(key)
            cell_before.next_node.key = key
            cell_before.next_node.value = value
        else:
            bucket_num = self._hash(key)
            linked_list = self.buckets[bucket_num]

            new_cell = Cell(key, value, linked_list.next_node)
            linked_list.next_node = new_cell

            self.num_elements += 1


if __name__ == '__main__':
    # with update
    ht_update = HashTableSeparateChainingWithUpdate(5)

    for key, value in map(lambda x: [int(x[1:4]), x],
                          ["B617KM39RUS", "B313AB39RUS", "C254HE39RUS", "E123OK39RUS",
                           "H617EA39RUS", "O313BA39RUS", "T254KP39RUS", "E123BT39RUS"]):
        ht_update.insert(key, value)

    print(ht_update)  # Ok, 4 unique cells

    # without update
    ht = HashTableSeparateChaining(5)

    for key, value in map(lambda x: [int(x[1:4]), x],
                          ["B617KM39RUS", "B313AB39RUS", "C254HE39RUS", "E123OK39RUS",
                           "H617EA39RUS", "O313BA39RUS", "T254KP39RUS", "E123BT39RUS"]):
        ht.insert(key, value)

    print(ht)  # raise ValueError
