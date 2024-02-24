class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    

    # For appending node in LL
    def append(self, value):
        new_node = Node(value)
        # If LL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If LL is not empty
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(4)
my_linked_list.append(44)
my_linked_list.append(444)
my_linked_list.print_list()

my_linked_list.reverse()
print("\nAfter reverse: \n")
my_linked_list.print_list()