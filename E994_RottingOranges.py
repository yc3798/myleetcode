# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

class Solution:
    def orangesRotting(self, grid) -> int:
        # BFS 
        n = len(grid)
        m = len(grid[0])
        count = 0
        q = [] 

        # list of rotten pos
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2: # rotten 
                    q.append((i,j))

        while q != []:
            temp = set()
            for t in q:
                grid, visited = self.visit(grid,t[0],t[1])
                temp = temp.union(visited)
            q = list(temp)
            if q:
                count += 1
        # print(grid)
        # print(count)

        # check for never rotten oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: # rotten 
                    return -1
        return count




                    
    def visit(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])
        q = set()
        
        if i-1 >= 0 and grid[i-1][j] == 1: #down
            grid[i-1][j] = 2
            q.add((i-1, j))
            
        if i+1 < n and grid[i+1][j] == 1: #up
            grid[i+1][j] = 2
            q.add((i+1, j))
            
        if j-1 >= 0 and grid[i][j-1] == 1: #left
            grid[i][j-1] = 2
            q.add((i, j-1))
            
        if j+1 < m and grid[i][j+1] == 1: #right
            grid[i][j+1] = 2
            q.add((i, j+1))
        # print("return q = ", q)
        return grid, q


grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid)) #4

grid=[[2,1,1],[0,1,1],[1,0,1]]
print(Solution().orangesRotting(grid)) #-1

grid=[[0,2]]
print(Solution().orangesRotting(grid)) #0
        