class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = [0] * 50
        for i in range(1, n+1):
            num = str(i)
            tmp = 0
            for j in num:
                tmp += int(j)
            cnt[tmp] += 1
        # print(cnt)
        a = max(cnt)
        ans = 0
        for i in cnt:
            if a == i:
                ans += 1

        return ans
    

res = Solution().countLargestGroup(13)
print(res)


res = Solution().countLargestGroup(2)
print(res)


res = Solution().countLargestGroup(15)
print(res)


res = Solution().countLargestGroup(24)
print(res)