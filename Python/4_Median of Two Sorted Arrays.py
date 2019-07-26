# /*
#  * @Author: JJ Luo 
#  * @Date: 2019-07-26 16:37:29 
#  * @Last Modified by:   JJ Luo 
#  * @Last Modified time: 2019-07-26 16:37:29 
#  */

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            i = int(len(nums) / 2)
            media =  (nums[i] + nums[i-1])/2.0
        else:
            i = int((len(nums)-1)/2)
            media = nums[i]
        return media

nums1 = [1, 2]
nums2 = [3, 4]
result = Solution().findMedianSortedArrays(nums1, nums2)
print(result)

nums1 = [1, 3]
nums2 = [2]
result = Solution().findMedianSortedArrays(nums1, nums2)
print(result)
