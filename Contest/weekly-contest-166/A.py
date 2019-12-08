class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        N = 0
        M = 1
        for i in s:
            N += int(i)
            M *= int(i)
        return M-N

res = Solution().subtractProductAndSum(234)
print(res)

res = Solution().subtractProductAndSum(4421)
print(res)