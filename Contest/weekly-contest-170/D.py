class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        def LCS(a,b):
            n = len(a)
            m = len(b)

            lcs = [[0] * (m+1) for i in range(n+1)]
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if a[i-1] == b[j-1]:
                        lcs[i][j] = 1 + lcs[i-1][j-1]
                    else:
                        lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            return lcs[n][m]

        n = len(s)

        if n == 0:
            return 0
        a = s
        b = s[::-1]
        return n - LCS(a, b)
    


s = "zzazz"
res = Solution().minInsertions(s)
print(res)

s = "mbadm"
res = Solution().minInsertions(s)
print(res)

s = "leetcode"
res = Solution().minInsertions(s)
print(res)

s = "g"
res = Solution().minInsertions(s)
print(res)

s = "no"
res = Solution().minInsertions(s)
print(res)

s = "ccewnxhytsr"
res = Solution().minInsertions(s)
print(res)

s = "swizunxvbbvjr"
res = Solution().minInsertions(s)
print(res)

