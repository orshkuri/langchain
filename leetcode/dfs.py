from typing import List


def dfs(n: int, source: int, target: int, connections: List[List[int]]) -> bool:
    stack = []  # append, pop
    visited = {i: False for i in range(n)}

    # put the source in the stack
    stack.append(source)

    while stack:
        u = stack.pop()
        if u == target:
            return True
        if not visited[u]:
            visited[u] = True  # mark visited
            neighbors = find_neighbors(u, connections)  # get u's neighbors
            stack += neighbors  # append the neighbors to the stack
    return False

def find_neighbors(source: int, connections: List[List[int]]) -> List[int]:
    neighbors = []
    for connection in connections:
        i, j = connection
        if i == source and j != source:
            neighbors.append(j)
        elif j == source and i != source:
            neighbors.append(i)
    return neighbors


connections = [[0,1],[1,2],[2,0],[1,3]]

val = dfs(n=4, source=3, target=1, connections=connections)
print(val)
