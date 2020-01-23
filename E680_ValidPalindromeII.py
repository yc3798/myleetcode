class Solution:
    
# Brute force: comparing all pairs
# O(n^2)
    def validPalindromeBF(self, s: str) -> bool:
        l = list(s)
        l.reverse()
        srev = "".join(l)
        if s == srev:
            return True
        
        for i in range(len(s)):
            if s[:i] + s[i+1:] == srev[:len(s) - 1 - i] + srev[len(s) - i:]:
                return True
        return False

# Greedy
# abccba 
# abcceba

# if head != tail: either remove head or tail
# if head == tail, i++, comparing next pos
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(word):
            return all(word[k] == word[len(word) - 1 - k] for k in range(len(word)//2))
        
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n - 1 - i]: # we either remove i or n - 1 - i 
                return isPalindrome(s[:i] + s[i+1:]) or isPalindrome(s[:n - 1 -i] + s[n - i:])
        return True
                