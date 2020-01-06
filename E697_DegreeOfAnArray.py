import collections

# Record the INDEXES of max-degree items in a hashtable {1:[0,1,3], 2:[3,8]....}, return min of range of all items
# Min = min(ht.items(), key = lambda x: x[1][-1] - x[1][0] + 1)
## Lambda function calculates the len of subarray 
# time: O(n)
# space O(n)
class Solution:
    def findShortestSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        freq = collections.Counter(nums)
        maxdegree = freq.most_common(1)[0][1]
        top = [i for i in freq if freq[i] == maxdegree] # maxdegree items
        d = {t:freq[t] for t in top} # maxdegree item: freq
        indexes = {t:[] for t in top} # maxdegree item : [indexes in nums]
        for i in range(len(nums)):
            if nums[i] in d and d[nums[i]] > 0:
                d[nums[i]] -= 1 # decrement the freq in d
                indexes[nums[i]].append(i)
                if d[nums[i]] == 0:
                    d.pop(nums[i])

        minlen = min(indexes.items(), key = lambda x : x[1][-1] - x[1][0] + 1)
        # print(minlen)
        # print(minlen[1][-1] - minlen[1][0] + 1)
        return minlen[1][-1] - minlen[1][0] + 1
Solution().findShortestSubArray([1,2,2,3,1])               
            