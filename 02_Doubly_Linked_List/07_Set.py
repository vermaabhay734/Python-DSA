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
    
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
    

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False



my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(12)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(33)


print('Doubly Linked List:')
my_doubly_linked_list.print_list()
print("-----")

print(my_doubly_linked_list.set_value(2, 25))
my_doubly_linked_list.print_list()
# print(my_doubly_linked_list.get(2))

