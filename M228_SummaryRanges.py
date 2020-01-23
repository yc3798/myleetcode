class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        intervals = [(nums[0], nums[0])] #(low, high)
        pos = 0
        for i in range(1, len(nums)):
            low, high = intervals[pos]
            
            if nums[i] - high == 1: # extend interval
                intervals[pos] = (low, high + 1)
            else:
                if low != high:
                    intervals[pos] = str(low) + "->" + str(high)
                else:
                    intervals[pos] = str(low)
                    
                intervals.append((nums[i], nums[i]))
                pos += 1
                
        low, high = intervals[pos]
        if low != high:
            intervals[pos] = str(low) + "->" + str(high)
        else:
            intervals[pos] = str(low)
            
        return intervals
            