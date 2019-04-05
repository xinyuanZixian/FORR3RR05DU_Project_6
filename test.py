class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self, d):
        if self.value == d:
            return False
        elif self.value > d:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return True
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return True


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True

    def preOrderPrint(self):
        if self.root:
            print(self.root.value)
            currnode = self.root
            if self.root.left and self.root.right:
                self.root = currnode.left
                self.preOrderPrint()
                self.root = currnode.right
                self.preOrderPrint()
            elif self.root.left:
                self.root = currnode.left
                self.preOrderPrint()
            elif self.root.right:
                self.root = currnode.right
                self.preOrderPrint()
                
            
                


t = Tree()
print(t.insert(50))
print(t.insert(30))
print(t.insert(70))
print(t.insert(20))
print(t.insert(40))
print(t.insert(60))
print(t.insert(80))
t.preOrderPrint()

