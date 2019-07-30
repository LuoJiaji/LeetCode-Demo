class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_2 = 1
        n_1 = 2
        if n == 1 :
            result = 1
        elif n == 2:
            result = 2
        else:
            for i in range(n-2):
                result = n_1 + n_2
                n_2 = n_1
                n_1 = result
                # print(n_2, n_1, result)
        # print(result)
        return result

result = Solution().climbStairs(5)
print(result)
