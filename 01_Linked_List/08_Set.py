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
    
    
    def get(self, index):
        if index<0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp   
    
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


my_linked_list = LinkedList(12)
my_linked_list.append(44)
my_linked_list.append(434)
my_linked_list.append(24)

my_linked_list.set_value(1,4)

my_linked_list.print_list()
