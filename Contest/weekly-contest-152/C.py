class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(s)
        f = [[0]*26 for _ in range(n+1)]

        for i in range(n):
            for j in range(26):
                f[i+1][j] = f[i][j]
            f[i+1][ord(s[i]) - ord('a')] += 1
        
        res = []

        for p, q, m in queries:
            t = 0
            for i in range(26):
                if (f[q+1][i]- f[p][i]) % 2 != 0:
                    t += 1
            res.append(m >= t//2)

        return res

s = "abcda"
queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
result = Solution().canMakePaliQueries(s, queries)
print(result)
