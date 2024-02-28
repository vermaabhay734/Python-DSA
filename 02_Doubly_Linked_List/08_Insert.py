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

    # For Appending node in DLL
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
    
    
    # For prepending node in DLL
    def prepend(self, value):
        new_node = Node(value)
        # If DLL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If DLL is not empty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
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

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1   
        return True  


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(12)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(33)


print('Doubly Linked List:')
my_doubly_linked_list.print_list()
print("-----")

my_doubly_linked_list.insert(1, 26)
my_doubly_linked_list.print_list()
