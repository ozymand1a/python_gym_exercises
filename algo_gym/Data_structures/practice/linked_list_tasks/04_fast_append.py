from algo_gym.Data_structures.theory.linked_list import List, Node


class ListWithFastAppend(List):
    def __init__(self):
        List.__init__(self)
        self.tail = None

    def append(self, value):
        if self.tail is not None:
            self.tail.next_node = Node(value)
            self.tail = self.tail.next_node
        else:
            self.top.next_node = Node(value)
            self.tail = self.top.next_node


if __name__ == '__main__':
    lst = ListWithFastAppend()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(lst.__str__())
