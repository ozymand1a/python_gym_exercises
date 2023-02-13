class Cell:
    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f"[{self.key}:{self.value}]"


class HashTableSeparateChaining:
    def __init__(self, size):
        self.size = size
        self.num_elements = 0

        self.buckets = [Cell(None, None, None) for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def _find_cell_before(self, key):
        """
        return before element by key or None
        """
        bucket_num = self._hash(key)

        top = self.buckets[bucket_num]

        cell = top
        while cell.next_node:
            if cell.next_node.key == key:
                return cell
            cell = cell.next_node

        return None

    def get(self, key):
        """
        return element by key
        """
        cell_before = self._find_cell_before(key)

        if not cell_before:
            return None

        return cell_before.next_node

    def insert(self, key, value):
        """
        insert at top Linked List
        """
        if self.get(key) is not None:
            raise ValueError(f"Key {key} is on the table.")

        bucket_num = self._hash(key)
        linked_list = self.buckets[bucket_num]

        new_cell = Cell(key, value, linked_list.next_node)
        linked_list.next_node = new_cell

        self.num_elements += 1

    def delete(self, key):
        cell_before = self._find_cell_before(key)

        if not cell_before:
            raise ValueError(f"Key {key} is not on the table.")

        cell_before.next_node = cell_before.next_node.next_node

        self.num_elements -= 1
        return None

    def __str__(self):
        text = ""
        for _, cell in enumerate(self.buckets):
            text += f"{_}:"
            cell = cell.next_node
            while cell is not None:
                text += f" {cell}"
                cell = cell.next_node
            text += "\n"
        return text

    def change_size(self):
        pass


if __name__ == '__main__':
    ht = HashTableSeparateChaining(10)

    for key, value in map(lambda x: [int(x[1:4]), x],
                          ["B617KM39RUS", "B313AB39RUS", "C254HE39RUS", "E123OK39RUS",
                           "H637EA39RUS", "O129BA39RUS", "T765KP39RUS", "E389BT39RUS",
                           "B204BA39RUS", "M001EC39RUS", "A973AA39RUS", "C349EP39RUS",
                           "C166OK39RUS", "H555HH39RUS", "K675KH39RUS", "E746OP39RUS",
                           "T162BA39RUS", "C130BE39RUS", "B498BE39RUS", "B516MK39RUS"]):
        ht.insert(key, value)

    print(ht)
