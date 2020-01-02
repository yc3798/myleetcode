class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True 
        
        j = len(s) - 1
        i = 0
        while i <= j: 
            # print(i,j)
            if not (s[i].isalpha() or s[i].isnumeric()):
                i+=1
                continue
            if not (s[j].isalpha() or s[j].isnumeric()):
                j-=1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True
