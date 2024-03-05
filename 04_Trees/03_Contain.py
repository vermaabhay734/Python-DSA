class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            elif new_node.value > temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True     
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True     
                temp = temp.right

    
    def contain(self, param):
        temp = self.root
        while temp is not None:
            if temp.value == param:
                return True
            elif param > temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    
bst = BinarySearchTree()
bst.insert(5)
bst.insert(1)
bst.insert(51)
bst.insert(15)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
print(bst.contain(1))
        