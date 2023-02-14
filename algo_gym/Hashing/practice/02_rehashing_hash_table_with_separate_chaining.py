from algo_gym.Hashing.theory.hashing_with_separate_chaining import Cell, HashTableSeparateChaining


class HashTableSeparateChainingWithRehashing(HashTableSeparateChaining):
    def __init__(self, size):
        HashTableSeparateChaining.__init__(self, size=size)

    def change_size(self, new_size):
        """
        change size of hash table and rehashing all elements
        """
        buckets_new = [Cell(None, None, None) for _ in range(new_size)]
        old_size = self.size
        self.size = new_size

        # put all cells to buckets_new
        for i in range(old_size):
            top = self.buckets[i]

            while top.next_node:
                # !!! we don't need to check keys for uniqueness, because we check it at insert part

                # extract cell
                cell = top.next_node
                key, value = cell.key, cell.value

                # create new cell at rehashing table
                bucket_num = self._hash(key)
                linked_list = buckets_new[bucket_num]

                new_cell = Cell(key, value, linked_list.next_node)
                linked_list.next_node = new_cell

                # next iteration
                top = top.next_node

        self.buckets = buckets_new


if __name__ == '__main__':
    # init hash table
    ht = HashTableSeparateChainingWithRehashing(5)

    for key, value in map(lambda x: [int(x[1:4]), x],
                          ["B617KM39RUS", "B313AB39RUS", "C254HE39RUS", "E123OK39RUS",
                           "H637EA39RUS", "O129BA39RUS", "T765KP39RUS", "E389BT39RUS"]):
        ht.insert(key, value)

    print(ht)

    # rehashing
    ht.change_size(7)
    print(ht)
