class Solution:
    # Brute force: 
    # T(n) = T(n-1) + sqrt(n) = n^3/2
    def countPrimesBF(self, n: int) -> int:
        def isPrime(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        
        res = 0
        for i in range(2, n):
            res += isPrime(i)
        return res
    
    # Use a list of length n to represent integers < n
    # from 2 -> sqrt(n), check if each isPrime(i)
    # if yes, mark all multiple of i to "NonPrime"
    # return number of cells that is not marked. 
    def countPrimes(self, n: int) -> int:
        count = [1 for i in range(n)] # 1: prime, 0 Non-prime
        if n < 2:
            return 0
        count[0] = 0
        count[1] = 0
        
        def isPrime(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        # 2 -> n 
        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime(i): # mark multiple of i to 0 
                k = i + i
                while k < n:
                    count[k] = 0
                    k += i
    
        return sum(count)