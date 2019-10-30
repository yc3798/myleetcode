class Solution:
    def isValid(self, s: str) -> bool:
        pairs =  {"(":")", "{":"}", "[":"]"}
        checklst = []
        if len(s) % 2 != 0:
            return False
        # "{[)]}"
        for p in s:
            if p not in pairs: # p is right paren
                if len(checklst) == 0 or checklst[-1] != p:
                    return False
                checklst.pop(-1)
            
            else:
                checklst.append(pairs[p])
        return len(checklst) == 0
                
            
