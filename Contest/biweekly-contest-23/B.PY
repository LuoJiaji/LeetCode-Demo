class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False
        cnt = {}
        for i in s:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        odd = 0
        for i in cnt:
            # print(i)
            if cnt[i] % 2 == 1:
                odd += 1
        # print(odd)
        # print(cnt)

        return odd <= k

s = "annabelle"
k = 2
res = Solution().canConstruct(s, k)
print(res)

s = "leetcode"
k = 3
res = Solution().canConstruct(s, k)
print(res)

s = "true"
k = 4
res = Solution().canConstruct(s, k)
print(res)

s = "yzyzyzyzyzyzyzy"
k = 2
res = Solution().canConstruct(s, k)
print(res)

s = "cr"
k = 7
res = Solution().canConstruct(s, k)
print(res)