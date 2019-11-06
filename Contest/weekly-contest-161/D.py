class Solution(object):
    def gcd(self, a, b):
        ans = a if b == 0 else self.gcd(b, a%b)
        return ans 
    
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        g = nums[0]
        for i in nums:
            g = self.gcd(i, g)
        if g == 1:
            return True
        return False

nums = [12,5,7,23]
res = Solution().isGoodArray(nums)
print(res)

nums = [29,6,10]
res = Solution().isGoodArray(nums)
print(res)

nums = [3,6]
res = Solution().isGoodArray(nums)
print(res)
