
# BFS: 最里层是depth 1 
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        queue = [(nestedList, 1)]
        values = {} # depth:value
        while queue != []:
            curr, depth = queue.pop()
            for item in curr:
                if item.isInteger(): # add to values
                    if depth in values:
                        values[depth] += item.getInteger()
                    else:
                        values[depth] = item.getInteger()
                else: # is nestedList 
                    queue.append((item.getList(), depth + 1))
        if values == {}:
            return 0
        maxdepth = max(list(values.keys()))
        res = 0
        for key,val in values.items():
            res += (maxdepth + 1 - key) * val
        return res