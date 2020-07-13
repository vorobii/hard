

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def show_list(self):
        if self.head is None:
            print('List is Empty')

        else:
            check = self.head
            while check is not None:
                print(check.data)
                check = check.next

    def add_back(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            check = self.head
            while check.next is not None:
                check = check.next
            check.next = new_node
        self.size += 1

    def add_by_index(self, data, index):
        check = self.head
        prev = self.head
        new_node = Node(data)
        i = 0
        if index == 1:
            self.head = Node(data)
            self.head.next = check
        else:
            while i < index - 1:
                if i == index - 2:
                    prev = check
                check = check.next
                i += 1
            prev.next = new_node
            new_node.next = check

    def del_by_index(self, index):
        i = 0
        check = self.head
        prev = self.head

        if index == 1:
            self.head = self.head.next
        else:

            while i < index-1:

                if i == index - 2:
                    prev = check

                check = check.next
                i += 1
            prev.next = check.next


test = LinkedList()


test.add_back(6)
test.add_back(3)
test.add_back(2)
test.add_back(1)
test.add_by_index(3, 2)
test.show_list()
print('new')
test.del_by_index(3)

test.show_list()


