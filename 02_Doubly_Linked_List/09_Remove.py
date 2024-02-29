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
    
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        # by using 2 variable
        # before = self.get(index-1)
        # after = self.get(index+1)
        # before.next = after
        # after.prev = before
        # self.length -= 1


        # by using 1 variable
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(12)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(33)


print('Doubly Linked List:')
my_doubly_linked_list.print_list()
print("-----")


my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()