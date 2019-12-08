class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        import math
        left = 1
        right = max(nums) + 1
        while left < right:
            tmp = 0
            mid = int((left+right)/2)
            for n in nums:
                tmp += math.ceil(n/mid)
                print(tmp)
            if tmp <= threshold:
                right = mid
            else:
                left = mid + 1
            print(left, right, mid, tmp)
        return min(left, right)

import math
print(math.ceil(1/2))    
# nums = [1,2,5,9]
# threshold = 6
# res = Solution().smallestDivisor(nums, threshold)
# print(res)

# nums = [2,3,5,7,11]
# threshold = 11
# res = Solution().smallestDivisor(nums, threshold)
# print(res)

# nums = [19]
# threshold = 5
# res = Solution().smallestDivisor(nums, threshold)
# print(res)

