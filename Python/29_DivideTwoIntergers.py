
#  @Author: JJ Luo 
#  @Date: 2019-07-26 10:36:09 
#  @Last Modified by:   JJ Luo 
#  @Last Modified time: 2019-07-26 10:36:09 
# 

class Solution(object):
    def divide(self, dividend, divisor):
        result = 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            flag = 1
        else:
            flag = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend-divisor >= 0:
            # result += 1
            tmp = divisor
            i = 0
            while dividend - tmp >= 0:
                dividend -= tmp
                result += 1 << i
                tmp <<= 1
                i += 1
            
        result = flag*result
        if result > 2**31-1 or result < -2**31:
            result = 2**31-1
        return result

print(Solution().divide(7,-3))
# print(2**31)