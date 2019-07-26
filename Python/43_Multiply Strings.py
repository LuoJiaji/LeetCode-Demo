# /*
#  * @Author: JJ Luo 
#  * @Date: 2019-07-26 13:54:34 
#  * @Last Modified by:   JJ Luo 
#  * @Last Modified time: 2019-07-26 13:54:34 
#  */


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2) )
        i = len(num1) - 1
        j = len(num2) - 1
        # print(i,j,result)
        while i >= 0:
            while j >= 0:
                # print(i,j,result)
                result[i+j+1] += (int(num1[i]) * int(num2[j])) % 10
                result[i+j] += int((int(num1[i]) * int(num2[j])) / 10)
                
                j -= 1
            i -= 1
            j = len(num2) - 1
        # print(result)
        i = len(result) - 1
        while i > 0:
            if result[i] >= 10:
                result[i-1] += int(result[i] / 10)
                result[i] = result[i] % 10
            i -= 1
        # print(result)

        num = 0
        for i in result:
            num = num*10 + i
        # print(num)
        return str(num)

num1 = '98'
num2 = '9'
result = Solution().multiply(num1, num2)
print(result)
num1 = '123'
num2 = '456'
result = Solution().multiply(num1, num2)
print(result)