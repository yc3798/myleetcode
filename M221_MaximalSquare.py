# Given a 2D binary matrix filled with 0's and 1's, 
# find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

class Solution:
    # Brute force: O((mn)^2)
    # since we need to check for every cell = 1,
    # in worst case, we have the lowerleft cell == 0
    def maximalSquareBF(self, matrix: List[List[str]]) -> int:
        if matrix == [] or len(matrix[0]) == 0:
            return 0
        
        maxwidth = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    width = 2
                    maxwidth = max(maxwidth , 1)
                    
                    while i + width <= m and j + width <= n:
                        square = True
                        for k in range(j, j + width):
                            if matrix[i + width - 1][k] == "0":
                                square = False
                                break
                        if square:
                            for k in range(i, i + width):
                                if matrix[k][j + width - 1] == "0":
                                    square = False
                                    break

                        if not square:
                            break
                        maxwidth = max(maxwidth, width) 
                        width += 1
                    
        return maxwidth ** 2     

    # dynamic programming O(mn) time and space
    # D[i,j] = min(D[i-1, j], D[i, j-1], D[i-1, j-1]) + 1 if M[i,j] == 1, else 0 
    # D: width of square ending at i,j 
    def maximalSquare(self, matrix) -> int:
        if matrix == [] or len(matrix[0]) == 0:
            return 0 

        D = [[int(k) for k in line] for line in matrix] # deep copy 
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        res = max(res, 1)

                    else: # i, j > 1
                        D[i][j] = min(D[i-1][j],D[i][j-1],D[i-1][j-1]) + 1
                        res = max(D[i][j], res)
        return res ** 2 # note that the problem asks for area 


