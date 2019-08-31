class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        from collections import Counter

        c = Counter(nums)
        s = c.most_common(k)

        res = []

        for i in s:
            res.append(i[0])
        return res
        
    
nums = [1,1,1,2,2,3]
k = 2
res = Solution().topKFrequent(nums, k)
print(res)


