from algo_gym.Data_structures.theory.linked_list import List, Node


class ListWithTopInsert(List):
    def prepend(self, value):
        current = self.top

        old_next_node = current.next_node
        current.next_node = Node(
            value=value,
            next_node=old_next_node
        )


if __name__ == '__main__':
    lst = ListWithTopInsert()
    lst.append("A")
    lst.append("B")
    lst.prepend("C")
    lst.prepend("D")
    print(lst)
