class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        m = len(needle)
        if m == 0 or haystack == needle:
            return 0
        if n == 0 or m > n: # handle empty strings or case that needle > haystack 
            return -1
        
        curr = 0
        i = 0
        j = 0
        while curr < n and j < m:
            if haystack[curr] == needle[j]:
                if j == m - 1:
                    return i                
                curr += 1
                j += 1

            else:
                i += 1
                curr = i
                j = 0

        return -1
        

