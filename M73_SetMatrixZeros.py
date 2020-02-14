class Solution:
        # O(mn) time since we at least need to examine every cell 
        # O(m + n) space since we to keep track which col and rows to set zero
        # use two dictionary to save which row/col indexes we want to set zero 
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        # O(m + n) space 
        rows = {i:False for i in range(m)}
        cols = {j:False for j in range(n)}
        for i in range(m):
            for j in range(n):
                
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True 
                
        for i in range(m):
            for j in range(n):   
                if rows[i] or cols[j]:
                    matrix[i][j] = 0 # set zero 
