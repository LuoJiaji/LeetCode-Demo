class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        # if n % 2 == 1:
        #     cnt = int()
        # print(int(n/2)+2)
        for i in range(1, int(n/2)+1):
            ans += [i, -i]
        # print(ans)
        if n % 2 == 1:
            ans += [0]
        return ans


res = Solution().sumZero(5)
print(res)

res = Solution().sumZero(3)
print(res)
        
res = Solution().sumZero(1)
print(res)