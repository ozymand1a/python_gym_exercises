from algo_gym.Data_structures.theory.linked_list_doubly import ListDoubly, NodeDoubly


class ListDoublyWithTopInsert(ListDoubly):
    def prepend(self, value):
        current = self.top

        new_node = NodeDoubly(value)
        old_next_node = current.next_node
        # next
        current.next_node = new_node
        new_node.next_node = old_next_node
        # prev
        if old_next_node is not None:
            old_next_node.prev_node = new_node
        new_node.prev_node = current


if __name__ == '__main__':
    lst = ListDoublyWithTopInsert()
    lst.prepend(1)
    lst.prepend(2)
    lst.prepend(3)
    print(lst.__str__())
