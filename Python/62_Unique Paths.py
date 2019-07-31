class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n < m:
            n, m = m, n
        step = n + m - 2
        n = n-1
        m = m-1
        a = 1
        for i in range(1, m+1):
            a *= i
        # print('a:', a, 1, m)

        b = 1
        for i in range(step-m+1, step+1):
            b *= i
        # print(b)
        # print('b:', b, step-m+1, step+1)
        # print(step,a,b,b/a)
        return int(b/a)



class Solution1:
    # @return an integer
    def uniquePaths(self, m, n):
        # if m < n:
        #     return self.uniquePaths(n, m)
        ways = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                ways[j] += ways[j - 1]
            print(ways)
        return ways[n - 1]

# result = Solution().uniquePaths(3,2)
# print(result)
# result = Solution().uniquePaths(2,3)
# print(result)
# result = Solution().uniquePaths(5,2)
# print(result)
# result = Solution().uniquePaths(2,3)
# print(result)
# result = Solution().uniquePaths(7,3)
# print(result)


result = Solution1().uniquePaths(5,3)
print(result)
result = Solution1().uniquePaths(3,5)
print(result)