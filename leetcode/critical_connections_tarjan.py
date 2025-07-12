from collections import defaultdict
from typing import List


def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    critical_connections: List[List[int]] = []
    discovery = [0] * n
    low = [0] * n
    visited = set()
    graph = defaultdict(list)

    for i, j in connections:
        graph[i].append(j)
        graph[j].append(i)

    def dfs(prev, cur, time):
        visited.add(cur)
        low[cur] = time
        discovery[cur] = time
        time += 1

        for next in graph[cur]:
            if next not in visited:
                dfs(cur, next, time)
            if prev != next:
                low[cur] = min(low[cur], low[next])
            if discovery[cur] < low[next]:
                critical_connections.append([cur, next])

    dfs(-1, 0, 0)

    return critical_connections


connections = [[0,1],[1,2],[2,0],[1,3]]
conns = criticalConnections(n=4, connections=connections)
print(conns)

node = (1,2)
i, j = node
print(i, j)
