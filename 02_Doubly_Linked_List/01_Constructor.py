# For creating new node in Doubly LL.
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


# For Creating Doubly LL
class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    # Print Doubly LL
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_doubly_linked_list = DoublyLinkedList(4)
print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length)

# print(my_doubly_linked_list.head.value)