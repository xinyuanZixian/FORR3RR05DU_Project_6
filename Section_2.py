triangle = open("p067_triangle.txt")
tree = [[int(y) for y in x.rstrip("\n").split(" ")] for x in triangle]
cache = []

def maximumPathSum(tree, depth):
    if depth >= 0:
        for i in range(len(tree[depth]) - 1):
            cache.append(max(tree[depth][i] + tree[depth - 1][i], tree[depth][i + 1] + tree[depth - 1][i]))
        tree[depth - 1] = cache.copy()
        cache.clear()
        return maximumPathSum(tree, depth - 1)
    else:
        return int(tree[0][0])
    
print(maximumPathSum(tree, len(tree) - 1))

