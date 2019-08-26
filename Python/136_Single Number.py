class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # print(nums)
        nums.sort()
        # print(nums)
        i = 0
        while i < len(nums) - 1 :
            # print(nums[i])
            
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2

        return nums[-1] 

data = [2,2,1]
result = Solution().singleNumber(data)
print(result)

data = [4,1,2,1,2]
result = Solution().singleNumber(data)
print(result)