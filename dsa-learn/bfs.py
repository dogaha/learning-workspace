# breadth first seach is a method of seaching non linear structures like trees/graphs
# Search neghbors based on order of discovery

# BFS benefits
#   Will always return shortest path
#   Clean level order traversal
#   way to explore everythinh

# Tree template
'''
from collections import deque
def bfs_tree(root):
    queue = deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        for child in node.children:
            if is_gola(child):
                return FOUND(child)
            queue.append(child)
    return  Not Found
'''

# When to Use
#   traversing a tree from top to bottom
#   care about depth, distance, or level
#   find closest node to root

# Graph Template
'''
def bfs_graph(root):
    queue = deque([root])
    visted = set([root])
    while len(queue) > 0:
        node = queue.popleft()
        for neightbor in get_neighborts(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add neighbor
        
'''

# when to use
#   working with grids, adjacency lists, or networks
#   strucutre can contain cycles or duplicate paths
#   need to find the shortest number of steps
#   exploring possible states

# BFS pattern
# 1. A queue for current layer of exploration
# 2. A loop to process each node
# 3. a branching step where nodes are added to queue

class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def level_order_traversal(root:Node) -> list[list[int]]:
    '''
    Given the root node of a B-tree.
    Return a list of the values found in each level
    EX: 1 => 2,3 => 4,5 | -,6 => -,7 | -,- | -,- | -,-
        [[1],[2,3],[4,5,6],[7]]
    '''
    result = []
    queue = deque([root])
    while len(queue) > 0:
        n = len(queue)
        node = queue.popleft()
        new_level = []
        # loop through entire level
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)
            # load children in order 
            for child in [node.left,node.right]:
                queue.append(child)
        result.append(new_level)
    return result

# got an memory usage exceeded error
# i beleive because it also checks coordinates already visited
def flood_fill_my(r:int,c:int,replacement:int,image:list[list[int]]) -> list[list[int]]:
    '''
    Given a 2d array, the row and column, and the replacement color (number).
    Return a new array that replaces all conneceted colors with new color.
    '''
    color = image[r][c]
    shape = (len(image),len(image[0]))
    queue = deque([(r,c)])
    result = image.copy()

    while len(queue) > 0:
        coordinate = queue.popleft()
        if image[coordinate[0]][coordinate[1]] == color:
            result[coordinate[0]][coordinate[1]] = replacement
            neighbors = [
                (coordinate[0],coordinate[1]+1),
                (coordinate[0],coordinate[1]-1),
                (coordinate[0]+1,coordinate[1]),
                (coordinate[0]-1,coordinate[1])
            ]
            for neighbor in neighbors:
                if 0 <= neighbor[0] < shape[0] and 1 <= neighbor[1] < shape[1]:
                    queue.append(neighbor)
    return result

def flood_fill_my(r:int,c:int,replacement:int,image:list[list[int]]) -> list[list[int]]:
    num_rows,num_cols = len(image),len(image[0])
    def get_neighbors(coord,color):
        row,col = coord 
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                if image[neighbor_row][neighbor_col] == color:
                    yield neighbor_row,neighbor_col
    def bfs(root):
        queue = deque([root])
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        r,c = root
        color = image[r][c]
        image[r][c] = replacement
        visited[r][c] = True
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node,color):
                r,c = neighbor
                if visited[r][c]:
                    continue
                image[r][c] = replacement
                queue.append(neighbor)
                visited[r][c]
    bfs((r,c))
    return image
