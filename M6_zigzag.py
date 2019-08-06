class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # brute force
        if numRows == 1:
            return s

        n = len(s)
        ans = ['' for i in range(numRows)]
        j = 0
        incre = True

        for i in range(n):
            ans[j] += s[i]

            if j == numRows - 1:
                j -= 1
                incre = False

            elif j == 0:
                incre = True
                j += 1
            else:
                if incre:
                    j += 1
                else:
                    j -= 1

        return ''.join(str(x) for x in ans)





