class Cell:
    """
    Ячейка для сортированного связного списка.
    """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


def bucket_sort(arr, num_buckets):
    buckets = []

    for i in range(num_buckets):
        buckets.append(Cell())

    # max value
    max_value = float("-inf")
    for i in range(len(arr)):
        max_value = max(max_value, arr[i])

    # items per bucket
    items_per_bucket = (max_value + 1) / num_buckets

    # distribute
    for value in arr:
        bucket_num = int(value / items_per_bucket)

        # insert at bucket
        after_me = buckets[bucket_num]
        while (after_me.next_node is not None) and (after_me.next_node.value < value):
            after_me = after_me.next_node
        cell = Cell(value, after_me.next_node)
        after_me.next_node = cell

    # rebuild arr
    index = 0
    for i in range(num_buckets):
        cell = buckets[i].next_node
        while cell:
            arr[index] = cell.value
            index += 1
            cell = cell.next_node


if __name__ == '__main__':
    arr = [7, 8, 5, 9, 4, 1, 3]
    print(arr)
    bucket_sort(arr, 4)
    print(arr)
