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
    

    def pop(self):
        # If DLL is empty
        if self.length == 0:
            return None
        temp = self.tail
        # If there is only 1 node in DLL
        if self.length == 1:
            self.head = None
            self.tail = None
        # If two or more node are available in DLL
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp


    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)


print('Doubly Linked List:')
my_doubly_linked_list.print_list()
print("-----")
my_doubly_linked_list.pop_first()

my_doubly_linked_list.print_list()


