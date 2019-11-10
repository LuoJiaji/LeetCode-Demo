class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans = []
        for i in range(low, high+1):
            if len(str(i)) == 1:
                ans.append(i)
            else :
                flag = True
                s = str(i)
                for n in range(1,len(s)):
                    if abs(int(s[n])- int(s[n-1])) != 1:
                        flag = False
                        break
                if flag == True:
                    ans.append(i)
        return ans
                       

low = 0
high = 21
res = Solution().countSteppingNumbers(low, high)
print(res)
