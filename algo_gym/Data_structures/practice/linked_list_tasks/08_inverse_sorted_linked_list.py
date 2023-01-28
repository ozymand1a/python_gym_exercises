from algo_gym.Data_structures.theory.linked_list import Node


class SortedListInverse:
    """
    Сортированный связный список.
    """
    def __init__(self):
        self.top = Node()

    def append(self, value):
        """
        Добавление нового элемента в сортированный однонаправленный список.
        Время работы O(N).
        """

        # Находим ячейку перед той, в которую будем вставлять новый элемент.
        current = self.top
        if current.next_node is None:
            current.next_node = Node(value)
        else:
            while current.next_node and current.next_node.value > value:
                current = current.next_node

            # Вставляем новую ячеку после current
            new_node = Node(value)
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        current = self.top.next_node
        values = '['

        while current is not None:
            end = ', ' if current.next_node else ''
            values += str(current) + end
            current = current.next_node

        return values + ']'


if __name__ == '__main__':
    lst = SortedListInverse()
    lst.append(4)
    lst.append(12)
    lst.append(7)
    lst.append(5)
    lst.append(42)
    lst.append(1)
    print(lst)
