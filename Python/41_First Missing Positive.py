class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        # data.sort()
        # print(data)

        result = 1
        while result in nums:
            result += 1
        print(result)

data = [1,2,0]
result = Solution().firstMissingPositive(data)

data = [3,4,-1,1]
result = Solution().firstMissingPositive(data)

data = [7,8,9,11,12]
result = Solution().firstMissingPositive(data)
