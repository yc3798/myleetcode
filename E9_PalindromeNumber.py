class Solution:
    # 1. converting to string, use recursion, time O(n), space O(n)
    # 2. return reverse(x) == x 
    # 3. WITHOUT CONVERTING TO STRING: repeat x % 10 to get reversed number, return number == x 
    #    total number of % operations = number of 10 based bit = log10 x -> O(log10 x)
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return self.helper(x)
    
    def helper(self, x):
        
        n = len(x)

        if n == 1:
            return True
        if n == 2:
            return x[0] == x[1]
        
        else:
            return x[0] == x[n-1] and self.helper(x[1:n-1])
