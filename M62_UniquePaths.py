class Solution:
    # dynamic programming 
    # P[i,j] = P[i-1,j] + P[i, j-1]
    # base case 
    # P[1, *] = P[*, 1] = 1
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        
        P = [[1 if i == 0 or j == 0 else None for i in range(n)] for j in range(m)]
        
        def count(row, col):
            if P[row][col] is not None:
                return P[row][col]
            
            q = count(row - 1,col) + count(row,col - 1)
            P[row][col] = q
            return q
        
        return count(m-1,n-1)