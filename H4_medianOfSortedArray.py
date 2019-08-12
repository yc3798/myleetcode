class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)
        even = True
        if (m + n) % 2 == 0:  # md: index of median
            md = (m + n) // 2 - 1
        else:
            even = False
            md = (m + n) // 2
        i = 0
        ans = 0
        while len(nums1) > 0 and len(nums2) > 0:
            if i == md:
                if not even:
                    # we arrive at median
                    return min(nums1[0], nums2[0])
                else:
                    if nums1[0] < nums2[0]:
                        ans += nums1.pop(0)
                    else:
                        ans += nums2.pop(0)
                    if len(nums1) > 0 and len(nums2) > 0:
                        return (ans + min(nums1[0], nums2[0])) / 2
                    elif len(nums1) > 0:
                        return (ans + nums1[0]) / 2
                    else:
                        return (ans + nums2[0]) / 2

            else:
                if nums1[0] < nums2[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
                i += 1
        # now one list must be emtpy so extend cost O(1)
        nums1.extend(nums2)
        if even:
            return (nums1[md - i] + nums1[md - i + 1]) / 2
        else:
            return nums1[md - i]
