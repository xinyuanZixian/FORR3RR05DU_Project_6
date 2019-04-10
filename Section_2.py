triangle = open("p067_triangle.txt")
lst = [[int(y) for y in x.rstrip("\n").split(" ")] for x in triangle]
cache = []

def maximumPathSum(lst, depth):
    if depth >= 0:
        for i in range(len(lst[depth]) - 1):
            cache.append(max(lst[depth][i] + lst[depth - 1][i], lst[depth][i + 1] + lst[depth - 1][i]))
        lst[depth - 1] = cache.copy()
        cache.clear()
        return maximumPathSum(lst, depth - 1)
    else:
        return int(lst[0][0])
    
print(maximumPathSum(lst, len(lst) - 1))
