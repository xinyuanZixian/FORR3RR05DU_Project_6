f = open('p067_triangle.txt','r')
data = [[int(y) for y in x.rstrip('\n').split(' ')] for x in f]

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
        
i = len(data) - 1        
while i >= 0:
    for j in range(len(data[i])):
        if i == len(data) - 1:
            data[i][j] = Node(data[i][j])
        else:
            data[i][j] = Node(data[i][j])
            data[i][j].left = data[i + 1][j]
            data[i][j].right = data[i + 1][j + 1]
    i-=1
        
def re(d):
    if d.left == None:
        print(d.data)
    else:
        print(d.data)
        re(d.left)

re(data[0][0])
