class Solution:
    # Two dictionaries
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split(" ") # split by space 
        if len(str) != len(pattern):
            return False
        d = {} # pattern: string
        drev = {} # string: pattern
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]]= str[i]
            else:
                if d[pattern[i]]!= str[i]:
                    return False
                
            if str[i] not in drev:
                drev[str[i]]= pattern[i]
            else:
                if drev[str[i]]!= pattern[i]:
                    return False
        return True