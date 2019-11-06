class Solution(object):
    def longestSubsequence(self, arr, d):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        m = {}
        ans = 0
        if d == 0:
            for a in arr:
                if a not in m:
                    m[a] = 0
                m[a] += 1
                ans = max(ans, m[a])
            return ans
        for a in arr:
            if a not in m:
                m[a] = 1
            if a-d in m:
                m[a] = max(m[a], m[a-d] + 1)
            ans = max(ans, m[a])
            # print(m)
        #print m
        return ans

arr = [1,2,3,4]
difference = 1
res = Solution().longestSubsequence(arr, difference)
print(res)

arr =  [1,3,5,7]
difference = 1
res = Solution().longestSubsequence(arr, difference)
print(res)

arr =  [1,5,7,8,5,3,4,2,1]
difference = -2
res = Solution().longestSubsequence(arr, difference)
print(res)

arr =  [10,-11,8,-1,-14,-5,7,15,7,-2,14,5,-3,-9,12,-9]
difference = 0
res = Solution().longestSubsequence(arr, difference)
print(res)
