
class SolutionDFS:
    def numIslands(self, grid):
        
        rows = len(grid)

        if rows == 0:
            return 0

        cols = len(grid[0])

        if cols == 0:
            return 0 

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    grid = self.dfs(grid,i,j,cols,rows)
                    print(grid)
        return count 



    def dfs(self, grid, i, j, col, row):
        # print(i,j)
        if (i < 0 or j < 0 or i >= row or j >= col):
            return grid 
        elif grid[i][j] == "0":
            return grid
        else:
            # set grid ij to 0
            grid[i][j] = "0"
            grid = self.dfs(grid, i + 1, j, col, row) # down 
            grid = self.dfs(grid, i, j + 1, col, row)
            grid = self.dfs(grid, i - 1, j, col, row) #  
            grid = self.dfs(grid, i, j - 1, col, row)
            # print(grid)
        return grid






class SolutionBFS:
    def numIslands(self):
        raise NotImplementedError

if __name__ == '__main__':
    s = SolutionDFS()
    lsimple = [["1","1","0"],["0","1","1"],["1","0","1"]]
    l = [["1","1","1","1","0"],["0","0","0","1","0"],["1","0","0","0","0"],["0","0","1","1","0"]]
    l3 = [["1","1","1"],["0","1","0"],["1","1","1"]]

    l4 = [["1","0","1","1","1"],
          ["1","0","1","0","1"],
          ["1","1","1","0","1"]]
    ans = SolutionDFS.numIslands(s,l4)
    print(ans)