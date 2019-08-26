class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0,float('-inf'))
        nums.append(float('-inf'))
        print(nums)
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i-1

data = [1]
result = Solution().findPeakElement(data)
print(result)
print()

data = [-2147483648]
result = Solution().findPeakElement(data)
print(result)

print(-2147483648 > float('-inf'))