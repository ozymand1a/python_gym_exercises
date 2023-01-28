from algo_gym.Data_structures.theory.linked_list_doubly import ListDoubly, NodeDoubly


class ListDoublyWithDelete(ListDoubly):
    def delete(self, value):
        current = self.top.next_node
        prev = self.top

        while current is not None:
            if current.value == value:
                next_node = current.next_node
                prev.next_node = current.next_node
                next_node.prev_node = prev
                return

            prev = current
            current = current.next_node


if __name__ == '__main__':
    lst = ListDoublyWithDelete()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(5)
    lst.append(9)
    print(lst.__str__())
    lst.delete(3)
    print(lst.__str__())
