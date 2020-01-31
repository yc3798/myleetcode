class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # for each candidate pattern, compare (k * pattern == s)
        # each comparison cost O(n) -> Total n^2
        n = len(s)
        for i in range(1, n//2 + 1):
            # check if length match
            if n % i == 0 and (n // i) * s[:i] == s:
                return True
        return False
            
# s = aabba|aabba -> True
# s = aba -> False
# s = a -> True