class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1: # last digit
                digits[i] += 1
            if carry == 1:
                carry = 0
                digits[i] += 1
            
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
                
        if carry == 1:
            digits.insert(0, 1)
        
        return digits
                    
                        
                    