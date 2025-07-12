from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        union_find = []
        node2island = {}
        current_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                node = (i, j)
                islands = self.find_islands(node, node2island, grid)
                #  if a new 1 node without neighbors
                if not islands and grid[i][j] == '1':
                    node2island[node] = current_island
                    union_find.append(current_island)
                    current_island += 1
                # if 1 with islands neighbors, unite the islands
                elif grid[i][j] == '1':
                    if len(islands) == 1:
                        island = islands[0]
                        island, _ = self.find(island, union_find)
                        node2island[node] = island
                    else:  # more than 1 neighbor islands, unite them
                        self.union(islands, union_find)
                        # find the correct island
                        island = islands[0]
                        island, _ = self.find(island, union_find)
                        node2island[node] = island


        return len(set([self.find(x, union_find)[0] for x in union_find]))

    def find_islands(self, node, node2island, grid) -> List[int]:
        i, j = node
        islands = []
        if i > 0:
            island = node2island.get((i - 1, j), -1)
            if island >= 0:
                islands.append(island)
        if i < len(grid):
            island = node2island.get((i + 1, j), -1)
            if island >= 0:
                islands.append(island)
        if j > 0:
            island = node2island.get((i, j - 1), -1)
            if island >= 0:
                islands.append(island)
        if j < len(grid[0]):
            island = node2island.get((i, j + 1), -1)
            if island >= 0:
                islands.append(island)
        return islands

    def find(self, idx, union_find):
        elements = []
        x = union_find[idx]
        elements.append(idx)
        while x != idx:
            elements.append(idx)
            idx = x
            x = union_find[idx]
        return x, elements

    def union(self, indices, union_find):
        heads = []
        all_elements = []
        for idx in indices:
            x, elements = self.find(idx, union_find)
            heads.append(x)
            all_elements += elements
        min_head = min(heads)
        for element in all_elements:
            union_find[element] = min_head


sol = Solution()
grid = [["1","0","1","1","0","0","1","0","1","1","1","1","0","1","0","1","1","1","1","0"],["0","1","0","0","1","0","1","0","1","1","1","1","1","1","0","1","1","0","1","1"],["1","0","0","1","0","1","0","1","0","1","1","0","1","1","1","0","0","1","1","0"],["0","1","1","0","0","1","1","0","1","1","1","1","0","0","1","0","0","0","1","1"],["1","1","0","1","0","0","1","0","0","0","1","0","1","0","1","1","1","0","1","1"],["0","0","0","0","1","0","1","1","0","0","1","0","0","1","0","1","1","1","1","0"],["1","0","1","1","1","1","0","1","1","0","1","1","0","1","1","1","0","0","1","0"],["0","1","1","0","0","0","1","0","0","1","0","1","1","1","0","0","1","1","0","1"],["0","0","0","0","1","1","0","1","0","0","1","1","0","1","0","0","1","0","1","0"],["0","0","1","1","1","0","1","0","1","0","1","1","1","0","1","1","1","1","1","0"],["1","0","1","0","1","1","1","0","1","1","1","0","1","0","1","0","1","0","1","1"],["0","0","1","1","1","1","0","1","1","1","0","1","0","0","0","1","1","1","0","1"],["1","1","1","0","0","0","0","0","1","1","0","1","1","1","0","1","1","1","1","0"],["0","0","1","1","1","0","0","1","0","0","1","1","1","1","1","1","0","1","1","0"],["0","0","0","1","1","0","0","0","0","1","1","0","1","0","0","1","1","1","1","1"],["0","1","1","1","0","1","0","0","1","1","1","1","1","0","1","1","1","0","0","1"],["0","0","0","0","1","1","1","1","0","0","0","0","1","0","0","0","0","1","1","0"],["1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1","1","1"],["0","1","0","0","1","0","0","1","1","1","1","1","1","0","1","0","1","1","1","1"],["0","0","1","1","1","1","1","0","0","0","1","1","1","1","1","1","0","1","1","0"]]
a = sol.numIslands(grid)
print(a)
