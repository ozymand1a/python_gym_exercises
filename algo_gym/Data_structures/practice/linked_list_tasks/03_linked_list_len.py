from algo_gym.Data_structures.theory.linked_list import List


class ListWithLength(List):
    """
    It is not optimal solution, but i don't want to rewrite parent class methods:)
    """
    def length(self):
        current = self.top.next_node
        len = 0

        while current is not None:
            len += 1
            current = current.next_node

        return len


if __name__ == '__main__':
    lst = ListWithLength()
    lst.append("A")
    lst.append("B")
    lst.append("C")
    print(lst.length())
