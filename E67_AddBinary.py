class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n, m = len(a), len(b)
        # prepend '0's  
        a = '0' * (max(n,m) - n) + a
        b = '0' * (max(n,m) - m) + b
        
        i = len(a) - 1 
        carry = 0
        res = ''
        while i >= 0:
            s = int(a[i]) + int(b[i]) + carry
            if s == 2:
                carry = 1
                s = 0
            elif s == 3:
                carry = 1
                s = 1
            else: # s = 0, 1 
                carry = 0
            i -= 1 
            res = str(s) + res
            
        if carry > 0:
            res = str(carry) + res
            
        return res