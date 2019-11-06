class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        ans = []
        t = start
        tmp = 0
        for i in range(1, (1 << n) + 1):
            ans.append(t)
            u = 1
            while not (i & u):
                u = u << 1
            tmp = tmp ^ u
            print(i, bin(i), t, bin(t), u, bin(u), bin(tmp))
            t = t ^ u

        return ans

n = 2
start = 3
res = Solution().circularPermutation(n, start)
print(res)

n = 5
start = 2
res = Solution().circularPermutation(n, start)
print(res)
