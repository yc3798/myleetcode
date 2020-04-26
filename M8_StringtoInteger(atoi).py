class Solution:
    def myAtoi(self, str: str) -> int:
        res, i, sign = 0, 0, 1 
        str = str.strip() # remove white space, optimize!
        minint, maxint = -2**31, 2**31 - 1
        
        while i < len(str):
            # print(str[i], res)
            if i == 0 and str[i] == '-':
                sign = -1
            elif i == 0 and str[i] == '+':
                sign = 1 
                
            else:
                n = ord(str[i]) - ord("0")
                if n >= 0 and n < 10:
                    increm = sign * n
                    # check for overflow 
                    if sign > 0:
                        if (maxint - increm) / 10 >= res:
                            res = res * 10 + increm 
                        else: # pos overflow 
                            return maxint
                    else:
                        if (minint - increm) / 10 <= res:
                            res = res * 10 + increm 
                        else: # neg overflow 
                            return minint
                        
                else: # invalid char
                    return res

            i += 1
        return res