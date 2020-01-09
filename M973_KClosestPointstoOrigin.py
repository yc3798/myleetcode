import math
class Solution:
# TODO: TRY USE A MIN HEAP and Divide and Conquer
# heap: O(klogn)

# use sort: O(nlogn)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K == 0:
            return []
        def dist(x):
            return math.sqrt(x[0] ** 2 + x[1] ** 2)
        points.sort(key = dist)
        return points[:K]
        