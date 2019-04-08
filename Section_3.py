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

    def preOrderPrint(self):
        print(self.value)
        if self.left and self.right:
            self.left.preOrderPrint()
            self.right.preOrderPrint()
        elif self.left:
            self.left.preOrderPrint()
        elif self.right:
            self.right.preOrderPrint()

    def postOrderPrint(self):
        if self.left and self.right:
            self.left.postOrderPrint()
            self.right.postOrderPrint()
        elif self.left:
            self.left.postOrderPrint()
        elif self.right:
            self.right.postOrderPrint()
        print(self.value)

    def delete(self, d):
        if d == self.value:
            if self.left and self.right:
                self.value = self.right.replaceableNode()
                if self.right.value == None:
                    self.right = None
                return True
            elif self.left:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
                return True
            elif self.right:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return True
            else:
                return False
        elif d > self.value and self.right:
            if self.right.value == d and self.right.left is None and self.right.right is None:
                self.right = None
                return True
            else:
                return self.right.delete(d)
        elif d < self.value and self.left:
            if self.left.value == d and self.left.left is None and self.left.right is None:
                self.left = None
                return True
            else:
                return self.left.delete(d)
        else:
            return False

    def replaceableNode(self):
        if self.left:
            if self.left.left:
                return self.left.replaceableNode()
            else:
                d = self.left.value
                if self.left.right:
                    self.left = self.left.right
                    return d
                else:
                    self.left = None
                    return d
        else:
            d = self.value
            if self.right:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return d
            else:
                self.value = None
                return d
                

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
            return self.root.preOrderPrint()
        else:
            return print(False)
                
    def postOrderPrint(self):
        if self.root:
            return self.root.postOrderPrint()
        else:
            return print(False)

    def delete(self, d):
        if self.root:
            if d == self.root.value:
                if self.root.right is None:
                    self.root = self.root.left
                    return True
                else:
                    self.root.value = self.root.right.replaceableNode()
                    return True
            else:
                return self.root.delete(d)
        else:
            return print(False)

    def deleteTree(self):
        if self.root:
            self.root = None
            return True
        else:
            return False


t = Tree()
print(t.insert(50))
print(t.insert(30))
print(t.insert(20))
print(t.insert(40))
print(t.insert(70))
print(t.insert(60))
print(t.insert(80))
print()
t.preOrderPrint()
print()
t.postOrderPrint()
print()
print(t.delete(20))
print()
t.preOrderPrint()
print()
t.postOrderPrint()
print()
print(t.delete(30))
print()
t.preOrderPrint()
print()
t.postOrderPrint()
print()
print(t.delete(50))
print()
t.preOrderPrint()
print()
t.postOrderPrint()
print()
print(t.deleteTree())
print()
t.preOrderPrint()
print()
t.postOrderPrint()
