# /*
#  * @Author: JJ Luo 
#  * @Date: 2019-07-26 13:53:54 
#  * @Last Modified by:   JJ Luo 
#  * @Last Modified time: 2019-07-26 13:53:54 
#  */

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] == target:
                return i
            elif nums[j] == target:
                return j
            else:
                i += 1
                j -= 1
        return -1
        

nums = [4,5,6,7,0,1,2]
target = 0
result = Solution().search(nums, target)
print(result)
nums =  [4,5,6,7,0,1,2]
target = 3
result = Solution().search(nums, target)
print(result)
nums =  [1]
target = 1
result = Solution().search(nums, target)
print(result)