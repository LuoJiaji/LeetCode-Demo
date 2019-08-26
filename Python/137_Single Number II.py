class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # print(nums)

        i = 0
        while i < len(nums)-1:

            if nums[i] != nums[i+1]:
                return nums[i]
            i += 3
        return nums[-1]


 


data = [2,2,3,2]
result = Solution().singleNumber(data)
print(result)

data = [0,1,0,1,0,1,99]
result = Solution().singleNumber(data)
print(result)