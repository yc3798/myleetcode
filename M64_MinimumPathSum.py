import sys
class Solution:
    def minPathSum(self, grid) -> int:
        # Dynamic Programming: use a m * n grid to track minimal path sum from 0, 0 to each cell: O(mn) time and space

        if grid == []:
            return 0
        m = len(grid)
        n = len(grid[0])

        # initialize D, D[i,j] = minimal path sum from i->j 
        D = [[sys.maxsize for i in range(n)] for j in range(m)]
        D[0][0] = grid[0][0]

        # populate values
        for i in range(m):
            for j in range(n):
                # check left and up grid in D
                if i - 1 >= 0:
                    D[i][j] = min(D[i - 1][j] + grid[i][j], D[i][j])
                if j - 1 >= 0:
                    D[i][j] = min(D[i][j - 1] + grid[i][j], D[i][j])
            # print(D)
        return D[m-1][n-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
Solution().minPathSum(grid)
