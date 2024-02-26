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


    def append(self, value):
        new_node = Node(value)
        # If Doubly LL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If Doubly LL is not empty
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)


print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')

print('Doubly Linked List:')
my_doubly_linked_list.print_list()
