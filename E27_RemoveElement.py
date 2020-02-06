class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    # idea: 
    # pos = -1, track position of the last valid element
    # if found valid elem, pos += 1, swap ok elements to pos
        pos = -1 
        for i in range(len(nums)):
            if nums[i] != val:
                pos += 1
                nums[pos], nums[i] = nums[i], nums[pos]
        return pos + 1
                
                

                