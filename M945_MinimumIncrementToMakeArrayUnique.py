class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()
        total = 0
        nextval = 0
        for num in sorted(A):
            if num not in s:
                s.add(num)
                nextval = num + 1
            else:
                total += nextval - num
                s.add(nextval)
                nextval += 1
        return total