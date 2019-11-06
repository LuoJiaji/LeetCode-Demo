class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        pre = [[0] * 16 for _ in range(6)]
        for i in range(6):
            pre[i][1] = 1
        for i in range(2, n+1):
            now = [[0] * 16 for _ in range(6)]
            for i in range(6):
                for j in range(1, 16):
                    if j + 1 <= rollMax[i]:
                        now[i][j+1] += pre[i][j]
                        now[i][j+1] = now[i][j+1] % mod
                    for k in range(6):
                        if k != i:
                            now[k][1] += pre[i][j]
                            now[k][1] = now[k][1] % mod
            print(now)
            pre = now
        return sum([sum(p)%mod for p in pre])%mod


n = 5
rollMax = [1,1,1,2,2,3]
res = Solution().dieSimulator(n, rollMax)
print(res)

