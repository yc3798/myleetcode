# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

class Solution:
    # Brute force recursion: O(2^n)
    # worst case "aaaaaaaaaaa", dict = a, aa, aaa, aaaa, aaaaa (n items in dict)
    # Problem 
    # runtime: T(n) = 2T(n-1) = O(2^n)

    # def wordBreakBF(self, s: str, wordDict) -> bool:
    #     return self.helper(s, wordDict)
    # def helper(self, s, wd):
    #     if s == "":
    #         return True
    #     for i in range(0, len(s)):
    #         # if s[0:i] in wordDict, recurse on the rest 
    #         if s[:i+1] in wordDict and self.wordBreak(s[i+1:], wordDict):
    #             return True
    #     return False        

    # recursion with memorization 
    def wordBreak(self, s, wordDict):
        n = len(s)
        mem = {i : None for i in range(n)}
        return self.helper(s, 0, wordDict, mem)

    def helper(self,s, start, wordDict, mem):
        n = len(s)
        # print(start)
        if start >= n :
            # print("return here")
            return True
        if mem[start] != None:
            return mem[start]
        for i in range(1, n - start + 1):
            if s[start : start + i] in wordDict: 
                if self.helper(s, start + i,wordDict, mem) is True:
                # print(start, i)
                # print(mem)
                    mem[start] = True
                    return True
                # print(mem)
                else:
                    mem[start] = False
                
        return False

# s = "applepenapple"
# wordDict = ["apple", "pen"]
# print(Solution().wordBreak(s,wordDict))
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# print(Solution().wordBreak(s,wordDict))
s = "aaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(Solution().wordBreak(s,wordDict))
