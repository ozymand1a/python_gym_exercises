class NodeDoubly:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value)


class ListDoubly:
    def __init__(self):
        self.top = NodeDoubly()

    def append(self, value):
        current = self.top

        while current.next_node is not None:
            current = current.next_node

        new_node = NodeDoubly(value)
        current.next_node = new_node
        new_node.prev_node = current

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


if __name__ == '__main__':
    lst = ListDoubly()
    lst.append(75)
    lst.append(12)
    lst.append(28)
    lst.append(6)
    print(lst)
