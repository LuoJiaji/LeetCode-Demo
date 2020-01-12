class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        i = 0
        l = len(nums)
        while i < l:
            
            ans += [nums[i+1]] * nums[i]
            i += 2
        return ans



nums = [1,2,3,4]
res = Solution().decompressRLElist(nums)
print(res)