class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
        # print(nums)
        res = ''
        for i in nums:
            res += str(i)

        # print(res)    
        if int(res) == 0:
            return str(0)    
        return res


data = [3,30,34,5,9]
result = Solution().largestNumber(data)
print(result)


data = [0, 0]
result = Solution().largestNumber(data)
print(result)