class Solution:
    # dynamic programming O(n)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = [0 for i in range(n + 1)]
        a[1] = 1
        a[2] = 2
        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2]
        return a[n]
            
        
    # Recursion(not optimal, repeating computation)
    # T(n) = T(n-1) + T(n-2), 
    # TODO: 用substitution 计算时间
    # T(n) = 2^n
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            # climb 1 step or 2 step
            return self.climbStairs(n - 1) + self.climbStairs(n-2)