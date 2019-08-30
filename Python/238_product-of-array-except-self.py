class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 1
        right = 1
        l = len(nums)
        res = [1] * l
        for i in range(l):
            res[i] = left 
            left *= nums[i]

        for i in reversed(range(l)):
            res[i] *= right
            right *= nums[i]

        return res


        


data = [1,2,3,4]
result = Solution().productExceptSelf(data)
print(result)