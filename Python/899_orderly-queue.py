class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K >= 2:
            s = sorted(S)
            s = ''.join(s)
            # print(s)
            return s
        else:
            s_min = S
            for _ in range(len(S)):
                S = S[1:] + S[0]
                s_min = min(s_min, S)
            return s_min


S = "cba"; K = 1
res = Solution().orderlyQueue(S, K)
print(res)

S = "baaca"; K = 3
res = Solution().orderlyQueue(S, K)
print(res)
