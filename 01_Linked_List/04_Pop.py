class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print LL
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


my_linked_list = LinkedList(4)
my_linked_list.append(34)

my_linked_list.print_list()
my_linked_list.pop()

print("---------------")
my_linked_list.print_list()


# print(my_linked_list.head.value)