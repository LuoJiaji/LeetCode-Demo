class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, sum_lr = 0, 0, 0
        min_l = len(nums)

        if sum(nums) < s:
            return 0

        while right < len(nums):
            while sum_lr < s and right < len(nums):
                sum_lr += nums[right]
                right += 1
            while sum_lr >= s:
                sum_lr -= nums[left]
                min_l = min(min_l, right-left)
                left += 1
                
                # if sum_lr >= s and min_l > right - left:
                #     min_l = right - left

        # print(min_l)
        return min_l
        
    
s = 7
nums = [2,3,1,2,4,3]
result = Solution().minSubArrayLen(s, nums)
print(result)

s = 11
nums = [1,2,3,4,5]
result = Solution().minSubArrayLen(s, nums)
print(result)

s = 3
nums = [1,1]
result = Solution().minSubArrayLen(s, nums)
print(result)

s = 5
nums = [2,3,1,1,1,1,1]
result = Solution().minSubArrayLen(s, nums)
print(result)
