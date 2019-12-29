class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [] or strs[0] == "":
            return ""
        if len(strs) == 1:
            return strs[0]
        return self.helper(strs, "")
    
    def helper(self, strs, prefix):
        if strs[0] == "":
            return prefix
        
        pf = strs[0][0]
        newstrs = [strs[0][1:]] #first element[1:] truncated
        
        for i in range(1,len(strs)):
            if strs[i] == "":
                return prefix
            if pf != strs[i][0]:
                return prefix
            else:
                newstrs.append(strs[i][1:])       
        return self.helper(newstrs, prefix + pf)
                    
