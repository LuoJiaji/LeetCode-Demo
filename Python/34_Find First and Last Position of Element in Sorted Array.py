# /*
#  * @Author: JJ Luo 
#  * @Date: 2019-07-26 15:46:42 
#  * @Last Modified by:   JJ Luo 
#  * @Last Modified time: 2019-07-26 15:46:42 
#  */

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        result = [-1, -1]
        # print(i,j)
        while i <= j:
            if nums[i] == target:
                result[0] = i
            else:
                i += 1
            if nums[j] == target:
                result[1] = j
            else:
                j -= 1
            # print(i,j,result)
            if nums[result[0]] == target and nums[result[1]] == target and result[0] != -1 and result[1] != -1:
                return result
        return result

nums = [5,7,7,8,10]
target = 8
result = Solution().searchRange(nums, target)
print(result)

nums = [1,4]
target = 4
result = Solution().searchRange(nums, target)
print(result)


