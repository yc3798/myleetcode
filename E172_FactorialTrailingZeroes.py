# find pattern 
# x <= 5: 5 * 4 = 20, 3 * 2 * 1 = 6
# 5 < x <= 10: 2 zeros 
# 10 < x <= 15: 2 + 1 zeros
# ... 
# + 1 zero for every 5
# note that we need to account for number that contains more 5's, for example, 25(5 * 5), 50(5 * 5 * 2)... 
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        
        else:
            return n // 5 + self.trailingZeroes(n//5)

        