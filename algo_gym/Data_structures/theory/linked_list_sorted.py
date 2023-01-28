class Node:
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

    def __str__(self):
        return str(self.value)


class SortedList:
    """
    Сортированный связный список.
    """

    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

        # Ограничитель
        self.top = Node()
        self.bottom = Node(1000)
        self.top.next_node = self.bottom

    def append(self, value):
        """
        Добавление нового элемента в сортированный однонаправленный список.
        Время работы O(N).
        """

        # Находим ячейку перед той, в которую будем вставлять новый элемент.
        current = self.top
        print(current.next_node)
        while current.next_node.value < value:
            current = current.next_node

        # Вставляем новую ячеку после current
        new_node = Node(value)
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.top.next_node
        values = "["

        while current is not None and current.value < 1000:
            end = ", " if current.next_node and current.next_node.value < 1000 else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


if __name__ == '__main__':
    lst = SortedList()
    lst.append(4)
    lst.append(12)
    lst.append(7)
    lst.append(5)
    print(lst)
