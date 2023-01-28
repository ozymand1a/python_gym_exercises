from algo_gym.Data_structures.theory.linked_list import List, Node


class ListWithMidInsert(List):
    def mid_insert(self, value, after_value):
        current = self.top.next_node

        while current is not None:
            if current.value == after_value:
                next_node = current.next_node
                current.next_node = Node(value)
                current.next_node.next_node = next_node

            current = current.next_node


if __name__ == '__main__':
    lst = ListWithMidInsert()
    lst.append(1)
    lst.mid_insert(2, 1)
    lst.mid_insert(3, 2)
    lst.mid_insert(45, 1)
    lst.mid_insert(7, 5)  # 5 в списке нет, значит 7 не будет добавлена
    print(lst.__str__())
