class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def hp(num):
            if num % 15 == 0:
                return "FizzBuzz"
            elif num % 5 == 0:
                return "Buzz"
            elif num % 3 == 0:
                return "Fizz"
            else:
                return str(num)
        ans = [hp(i) for i in range(1, n+1)]
        return ans
        
