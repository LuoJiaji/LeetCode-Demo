class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        curr = [0] *1000
        pre = [0] * 1000
        pre[0] = 1
        pre[1] = 1
        for _ in range(1,steps):
            ind = 0
            while ind <= min(arrLen - 1, _+2):
                if ind != 0:
                    curr[ind] += pre[ind-1]
                
                curr[ind] += pre[ind]
                
                if ind != arrLen - 1:
                    curr[ind] += pre[ind+1]
                ind += 1
            print(curr)
            pre = curr
            curr = [0] * 1000
        return pre[0] % 1000000007
                         
steps = 3
arrLen = 2
res = Solution().numWays(steps, arrLen)
print(res)

steps = 2
arrLen = 4
res = Solution().numWays(steps, arrLen)
print(res)

steps = 4
arrLen = 2
res = Solution().numWays(steps, arrLen)
print(res)

steps = 4
arrLen = 3
res = Solution().numWays(steps, arrLen)
print(res)