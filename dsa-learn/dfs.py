# DFS is going deep, fully explore a single branch

# Uses
# explore every possibility
# Visit Every ndoe
# Care about structure over distance

# DFS with Trees
# keep going until current node is noe
# return and go left once returned return and go back 
# Uses for
# Flattening Trees
# Building or Checking Structures
# Searching for nodes based on custom logic

# DFS with Graphs
# Must track visted nodes to avoid loops

class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root:Node) -> int:
    def dfs(root):
        if not root:
            return 0
        return max(dfs(root.left),dfs(root.right)) +1

def num_islands(grid:list[list[int]])->int:
    '''
    Count the numebr of islands that appear in given 2d list of 0s and 1s.
    Find the number of islands
    '''
    n = len(grid)
    m = len(grid[0])
    def get_neighbors(coord):
        result = []
        row, col = coord
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]

        for i in range(len(delta_row)):
            r = row + delta_row
            c = col + delta_col
            if 0<=r<m and 0<=c<n:
                result.append([r,c])
        return result
    def dfs(coord):
        r,c = coord
        if grid[r][c] == 0:
            return
        grid[r][c] = 0
        for neighbor in get_neighbors(coord):
            nr,nc = neighbor
            if grid[nr][nc] == 1:
                dfs(neighbor)

    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                dfs((r,c))
                counter+=1
    return count