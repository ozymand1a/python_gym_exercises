from algo_gym.Data_structures.theory.linked_list import List


class ListWithFind(List):
    def find(self, value):
        current = self.top

        while current is not None:
            if current == value:
                return

            current = current.next_node


if __name__ == '__main__':
    lst = ListWithFind()
    lst.append(3)
    lst.append(5)
    lst.append(7)
    lst.append(12)
    print(lst)
