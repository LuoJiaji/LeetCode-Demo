class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        freq = {}
        maxn = 0
        count = 0
        ans = 0
        for i in range(len(nums)):
            n = nums[i]
            if n not in m:
                m[n] = 0
            m[n] += 1
            f = m[n]
            if f not in freq:
                freq[f] = 0
            freq[f] += 1
            maxn = max(maxn, f)
            if f-1 > 0:
                freq[f-1] -= 1
            if f-1 in freq and freq[f] == 1 and freq[f] + freq[f-1] == len(m):
                ans = i+1
            if f+1 in freq and freq[f+1] == 1 and freq[f] + freq[f+1] == len(m):
                ans = i+1
            if freq[1] == 1 and (1 + freq[maxn] == len(m)):
                ans = i+1
            if  (maxn == 1 and freq[maxn] == len(m)):
                ans = i+1
            # print(m, freq, maxn,f,ans)
            
        return ans

nums = [2,2,1,1,5,3,3,5]
res = Solution().maxEqualFreq(nums)
print(res)
