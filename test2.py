triangle = open("p067_triangle.txt","r")
tree = [[int(y) for y in x.rstrip("\n").split(" ")] for x in triangle]
cache = []

def maximumPathSum(tree, depth):
    i = 0
    #while i >= len(tree[depth]) - 1:
        #d = max(tree[depth][i] + tree[depth - 1][i], tree[depth][i + 1] + tree[depth - 1][i])
    return max(tree[depth][i] + tree[depth - 1][i], tree[depth][i + 1] + tree[depth - 1][i])


print(maximumPathSum(tree, len(tree) - 1))
#https://blog.dreamshire.com/project-euler-67-solution/
