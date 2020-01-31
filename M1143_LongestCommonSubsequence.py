
# 1. Recursion with mem(top-down):
# if t1[i] == t2[i]:
#     return 1 + LSC(t1[1:], t2[1:])
# else 
#     return max(LSC(t1[], t2[1:]),LSC(t1[1:], t2[])) 

class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        mem = [[None for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        def lcs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if mem[i][j] != None:
                return mem[i][j]
            
            elif text1[i] == text2[j]:
                mem[i][j] = 1 + lcs(i + 1, j + 1)
                return mem[i][j]
            
            else:
                mem[i][j] = max(lcs(i, j + 1), lcs(i + 1, j)) 
                return mem[i][j]
        lcs(0,0)
        # mem[0,0] = LCS from t1[0] and t2[0]
        return mem[0][0]

# Dynamic Prog Bottom up: 
# lcs[i][j] = lcs of text1[1...i] and text2[1...j]
# base case: lcs[0][:] = 0, lcs[:][0] = 0
# if text1[i] == text2[j]
# lcs[i,j] = lcs[i-1][j-1] + 1
# else:
# lcs[i,j] = (max(lcs[i-1][j] + lcs[i-1][j])
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        lcs = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):

                t1 = text1[i - 1]
                t2 = text2[j - 1]
            
                if t2 == t1: # current char matches 
                    lcs[i][j] = lcs[i - 1][j - 1]+ 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        return lcs[-1][-1]