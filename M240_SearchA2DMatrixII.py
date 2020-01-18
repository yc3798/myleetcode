
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]

# Given target = 5, return true.

# Given target = 20, return false.


# 1. search each cell once  O(mn) 
class SolutionBF:
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if target in row:
                return True
        
        return False
# TODO: 2. Binary serach
class SolutionBS:
    def searchMatrix(self, matrix, target):

# 3. Divide and Conquer
class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == [[]] or matrix == []:
            return False
        return self.helper(matrix, 0, len(matrix[0]), 0, len(matrix), target)

    def helper(self, M, col_low, col_high, row_low, row_high, k):
        # out of boundary
        if col_low < 0 or col_high > len(M[0]) or row_low < 0 or row_high > len(M) or M[row_low][col_low] > k or M[row_high - 1][col_high - 1] < k:
            return False
        
        # one cell
        if col_low == col_high - 1 and row_low == row_high - 1: 
            return M[row_low][col_low] == target

        # find the pos s.t M[row_low][pos] < target < M[pos, row_high] 
        pos = col_low
        col_mid = (col_high - col_low) // 2

        for i in range(col_low + 1, row_high):
            if M[i][col_mid] == k:
                return True
            if M[i-1][col_mid] < k and M[i][col_mid] > k:
                pos = i
                break

        if M[row_high - 1][col_mid] < k:
        	pos = row_high
        # now we break down matrix around pos into 4 parts, 
        # and continue search in lower-left, upper-right submatrix

        # < k | ok
        # ----|----
        # ok  | > k
        return self.helper(M, col_low, col_mid, pos, row_high, k) or self.helper(M, col_mid, col_high, row_low, pos, k)
