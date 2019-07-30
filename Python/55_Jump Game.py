class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # pos = 0
        reachable = 0
        if len(nums) == 1:
            return True
        for i in range(len(nums)):
            reachable = max(i + nums[i], reachable)
            # print(i,reachable)
            if i >= reachable and i != (len(nums)-1):
                return False
        return True

data = [2,3,1,1,4]
result = Solution().canJump(data)
print(result)

data = [2,3,1,0,4]
result = Solution().canJump(data)
print(result)

data = [0]
result = Solution().canJump(data)
print(result)

data = [2,0,0]
result = Solution().canJump(data)
print(result)