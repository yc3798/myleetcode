class Solution:

    # 2. Sliding window : O(2n) = O(n)
    # sliding window is one-way, so each char visited max twice
    # worst case : "aaaaaa"
    def lengthOfLongestSubstring2(self, s:str) -> int:
        # raise NotImplementedError
        ans = 0
        i = 0
        j = 0
        n = len(s)
        myset = set()
        while i < n and j < n:
            if not s[j] in myset:
                myset.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                myset.remove(s[i])
                i += 1
        return ans


    # 1. Brute force with set
    #    runtime O(n^3)
    #       for each i, loop from i+1 to len(s) =>
    #       sum(i->n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        acc = 0
        chars = set([x for x in s])
        while len(s) != 0 and i < len(s):
            if max(longest,acc) > len(s):
                return max(longest,acc)
            if s[i] in chars:
                chars.remove(s[i])
                acc += 1
                i += 1
                longest = max(longest,acc)
            else:
                longest = max(longest,acc)
                chars = set(x for x in s[s.index(s[i])+1: ])
                s = s[s.index((s[i]))+1:]
                i = 0
                acc = 0
        return longest

#     def isUnique(self, s:str, i:int, j:int):
#         myset = set()
#         while i < j:
#             if s[i] in myset: # repeat, return false
#                 print("return false when i, j = ", i, j)
#                 return False, i
#             myset.add(s[i])
#             i += 1
#             print("i, j = ", i, j)
#         return True, i