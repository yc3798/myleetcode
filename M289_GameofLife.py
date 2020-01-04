# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
# i = 1
# < 2 neighbors 1, Die -> 0 
# 2, 3 neighbors 1, Live -> 1
# > 3 neighors 1, Die ->

# i = 0
# 3 neighbors 1, Live -> 1 
# Example:
# Input: 
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output: 
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

# Follow up:
# Could you solve it in-place? Remember that the board needs to be updated at the same time: 
# You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, 
# which would cause problems when the active area encroaches the border of the array. How would you address these problems?
import collections
class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # use a hashmap to check if a node need to flip 
        if board  == []:
            return board
        n = len(board)
        m = len(board[0])
        flip = {[i,j] : False for i in range(n) for j in range(m)}

        for i in range(n):
            for j in range(m):
                neighors = self.validNeighbors(self, n, m, i, j)
                nstatus = [board[i[0]][i[1]] for i in neighors]
                nstatus = collections.Counter(nstatus)
            if board[i][j] == 0 and nstatus[1] == 3:
                flip[i, j] = True

            else: # board[i][j] == 1 
            # < 2 neighbors 1, Die -> 0 
            # 2, 3 neighbors 1, Live -> 1
            # > 3 neighors 1, Die ->
                if nstatus[1] < 2 or nstatus[1] > 3:
                    flip[i,j] = True

        y = lambda x : 0 if x == 1 else 1
        board = [[y(board[i][j]) if flip[i][j] else board[i][j] for i in range(n)] for j in range(m)]
        print(board)

    def validNeighbors(self, n, m, i, j):
        d = {up:[i-1,j], down:[i+1, j], left:[i, j-1], right:[i, j+1], ul:[i-1, j-1], ur:[dl, dr]}
        if i == 0:
            del d[up]
            del d[ul]
            del d[ur]
        if j == 0:
            del d[left]
            del d[ul]
            del d[dl]
        if i == n - 1:
            del d[down]
            del d[dl]
            del d[dr]
        if j == m - 1:
            del d[right]
            del d[ur]
            del d[dr]
        neighors = list[d.items()]
        return [i[1] for i in neighors]



