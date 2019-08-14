
class SolutionDFS:
    def numIslands(self):
        raise NotImplementedError


class SolutionBFS:
    def numIslands(self):
        raise NotImplementedError

# ======== Naive approach ========
# Idea similar to DFS
class Solution:
    def numIslands(self, grid) -> int:
        """
        110
        011
        101
        """
        # Idea:
        # every pos goes to "visited"
        # if find "1", go through all its neighbors until all are "0"s
        # iterate the rest "unvisited" pos to find next 1
        # repeat until "unvisited" is empty
        self.printGrid(grid)
        row = len(grid)
        col = len(grid[0])
        unvisited = set()
        for i in range(row):
            for j in range(col):
                unvisited.add((i, j))
        # print(unvisited)
        ini = self.getNeighbors(0, 0).intersection(unvisited)

        return self.countHelper(unvisited, grid, 0, 0, 0, False, ini)

    def printGrid(self, grid):
        for i in grid:
            print(i)

    def specialCase(self, grid, row, col):
        raise NotImplementedError

    def countHelper(self, unvisited, grid, i, j, count, isfound, neighbors):
        """
        return

        110
        011
        101
        """

        # if 1 and not found -> count+= 1, add its neis, change found = True
        # if 1 -> add its getNeighbors().intersect(unvisited) to neighbors
        # if 0 and neighbors not empty -> pop next neighbour
        # if 0 and nei empty -> try next unvisited, set found = False
        # remember to rm from unvisited as visiting

        # print("->  i, j ", i, j)
        # print("unvisited ", unvisited)
        # print("nei: ", neighbors)

        if len(unvisited) == 0:
            return count

        if i is None and j is None:
            i, j = unvisited.pop()
        else:
            unvisited.remove((i, j))

        print(i, j, grid[i][j])


        if grid[i][j] == '1':
            if not isfound:
                isfound = True
                count += 1
                neighbors = self.getNeighbors(i, j).intersection(unvisited)

            else:
                isfound = True
                neighbors = neighbors.union(self.getNeighbors(i, j).intersection(unvisited))
                if len(neighbors) == 0:
                    isfound = False

            if len(neighbors) > 0:
                i, j = neighbors.pop()
            else:
                i, j = None, None
        else:  #grid[i][j] == '0'
            if len(neighbors) > 0: # pop from unvisited
                i, j = neighbors.pop()
            else:
                isfound = False
                i, j = None, None
        return self.countHelper(unvisited, grid, i, j, count, isfound, neighbors)

    def getNeighbors(self, i, j):
        return {(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)}
#

if __name__ == '__main__':
    s = Solution()
    lsimple = [["1","1","0"],["0","1","1"],["1","0","1"]]
    l = [["1","1","1","1","0"],["0","0","0","1","0"],["1","0","0","0","0"],["0","0","1","1","0"]]
    ans = Solution.numIslands(s,l)
    print(ans)