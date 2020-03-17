class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # brute force 
        # use a dictionary to record all restaurant:[indexes]
        # find min 
        # O(n + m) time and O(max(n,m)) space
        d = {list1[i]: i for i in range(len(list1))} # restaurant: indexes
        minsum = sys.maxsize
        res = []
        for i in range(len(list2)):
            if list2[i] in d:
                if d[list2[i]] + i == minsum:
                    res.append(list2[i])
                elif d[list2[i]] + i < minsum:
                    minsum = d[list2[i]] + i
                    res = [list2[i]]
        return res