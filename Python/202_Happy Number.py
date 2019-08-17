class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n)
        hn = 0
        while hn != 1:
            hn = 0
            for i in range(len(s)):
                # print(i,len(s))
                hn += int(s[i])**2
                # print(hn)
            s = str(hn)
            # print(hn)

            if hn == 4:
                return False
        return True

result = Solution().isHappy(19)
print(result)
result = Solution().isHappy(101)
print(result)