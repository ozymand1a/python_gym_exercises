from algo_gym.Data_structures.theory.linked_list import List


class ListWithFind(List):
    def find(self, value):
        current = self.top

        while current.next_node is not None:
            if current.value == value:
                return True

            current = current.next_node

        return False


if __name__ == '__main__':
    lst = ListWithFind()
    lst.append(3)
    lst.append(5)
    lst.append(7)
    lst.append(12)
    print(lst)
    print(lst.find(5))
    print(lst.find(42))
