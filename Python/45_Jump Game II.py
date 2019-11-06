# /*
#  * @Author: JJ Luo 
#  * @Date: 2019-07-28 18:50:34 
#  * @Last Modified by:   JJ Luo 
#  * @Last Modified time: 2019-07-28 18:50:34 
#  */


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jump_count = 0
        reachable = 0
        curr_reachable = 0

        for i, length in enumerate(nums):

            if i > reachable:
                return -1
            if i > curr_reachable:
                curr_reachable = reachable
                jump_count += 1            
        
            reachable = max(reachable, i + length)

        return jump_count

data = [2,3,1,1,4]
result = Solution().jump(data)
print(result)

