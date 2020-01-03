# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

# Attempt 1: 
# Idea similar to DFS
# Problem
# 1. many repeated visits
# 2. DFS trace update not correct 
class Solution:
    def exist(self, board, word):
        n = len(board)
        m = len(board[0])
        if board == []:
            return False
        
        for i in range(n):
            for j in range(m):
                track = [[0 for i in range(m)] for j in range(n)]
                if self.helper(i,j,board,word, track):
                    return True
        return False

    def helper(self, i, j, board, word, track):
        n = len(board)
        m = len(board[0])

        if word == "":
            return True

        if i >= n or i < 0 or j < 0 or j >= m:
            return False
        
        if track[i][j] == 0 and board[i][j] == word[0]:
            track[i][j] = 1 # set to empty
            for line in track:
                print(line)
            # check other dir 
            if self.helper(i+1, j, board, word[1:],track) or self.helper(i-1, j, board, word[1:],track) or self.helper(i, j-1, board, word[1:],track) or self.helper(i, j+1, board, word[1:],track):
                return True
            else:
                track[i][j] = 0

        return False
                    




# myboard = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
# # ABCE
# # SFCS
# # ADEE

# w1 = "ABCCED" # true.
# w2 = "SEE" # true.
# w3 = "ABCB"  # false.

# print(Solution().exist(myboard, w1))
# print(Solution().exist(myboard, w2))
# print(Solution().exist(myboard, w3))

# myboard2 = [["C","A","A"],["A","A","A"],["B","C","D"]]
# # CAA
# # AAA
# # BCD

# w4 = "AAB"
# print(Solution().exist(myboard2, w4))


# [["A","B","C","E"],
#  ["S","F","E","S"],
#  ["A","D","E","E"]]

myboard3 = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
w5 = "ABCESEEEFS"
print(Solution().exist(myboard3, w5))