class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

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
        
    def pop(self):
        # If LL is empty
        if self.length == 0:
            return None
        # If two or more node are available in LL
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next 
            self.tail = pre
            # For popping last one
            self.tail.next = None
            self.length -= 1
            # If there is only 1 node in LL
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp


    def popfirst(self):
        # If LL is empty
        if self.length == 0:
            return None
        # If two or more node are available in LL
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            # If there is only 1 node in LL
            if self.length == 0:
                self.tail = None
            return temp



    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        

    def removeValue(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            return self.popfirst()
        temp = self.head
        pre = None
        while temp is not None:
            if value == temp.value:
                # temp = pre.next
                pre.next = temp.next
                temp.next = None
                self.length -= 1
                return True
            else:
                pre = temp
                temp = temp.next
        return False

        

my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(34)
my_linked_list.append(2)
my_linked_list.append(7)
my_linked_list.append(29)


print('LL before insert():')
my_linked_list.print_list()
print("--")
print(my_linked_list.removeValue(29))

print('\nLL after remove in middle:')
my_linked_list.print_list()
