
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build two dictionary, letter:first index, letter:count
        firstindex = {}
        count = {}
        if s == '':
            return -1
        if len(s) == 1:
            return 0
        
        for i in range(len(s)):
            if not s[i] in count:
                firstindex[s[i]] = i
                count[s[i]] = 1
            else:
                count[s[i]] += 1
                if s[i] in firstindex:
                    del firstindex[s[i]]
        
        if len(firstindex) == 0:
            return -1
        return min(firstindex.items(), key = lambda x:x[1])[1]
