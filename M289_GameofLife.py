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
        # make a copy of original board
        cp = [[j for j in i] for i in board]
        neighors = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1],[1,-1],[-1,1]]
        for i in range(n):
            for j in range(m):
                count = 0 # count alive neighbors
                neig = [[i + x[0], j + x[1]] for x in neighors]
                for x in neig:
                    # check range valid
                    if x[0] >= 0 and x[0] < n and x[1] >= 0 and x[1] < m:
                        count += board[x[0]][x[1]]
                # case 1, cell = 0 and 3 live neighbors  
                if board[i][j] == 0 and count == 3:
                    cp[i][j] = 1

                # case cell = 1
                if board[i][j] == 1:
                    # < 2 neighbors 1, Die -> 0 
                    # 2, 3 neighbors 1, Live -> 1
                    # > 3 neighors 1, Die -> 0
                    if count < 2 or count > 3:
                        cp[i][j] = 0
        for i in range(n):
            for j in range(m):
                board[i][j] = cp[i][j]
Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])

