class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return ''
        n = 0
        while 1:
            if 2**n - 1 > num:
                break
            n += 1
        # print(n)
        # print(ans[2:])

        ans = bin(num - 2**(n-1) + 1)[2:]
        # print(ans)
        if len(ans) != n-1:
            ans = '0' * (n-1-len(ans)) + ans
        # if len(ans)  
        return ans

num = 23
res = Solution().encode(num)
print(res)

num = 107
res = Solution().encode(num)
print(res)

num = 3
res = Solution().encode(num)
print(res)