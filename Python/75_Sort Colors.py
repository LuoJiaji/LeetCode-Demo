class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        point = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0 and  point < i:
                if nums[point] == 0:
                    point += 1
                elif point == i:
                    i += 1
                else:
                    nums[point], nums[i] = nums[i], nums[point]
                    i += 1
                    point += 1
            else:
                i += 1
        # print(nums, point,i)
        # point += 1
        i = point
        while i < len(nums):
            # print('point:',point)
            if nums[i] == 1 and point < i:
                if nums[point] == 1 or nums[point] == 0:
                    point += 1
                elif point == i:
                    i += 1
                else:
                    nums[point], nums[i] = nums[i], nums[point]
                    i += 1
                    point += 1
                # print(nums, point,i)
                    # point += 1
            else:
                i += 1
        # print(nums, point)
        return nums

data = [2,0,2,1,1,0]
result = Solution().sortColors(data)
print(result)

data = [2,0,1,0,1,0,0,0,2,1,1,0,1,2,0,0,1,1,1,2]
result = Solution().sortColors(data)
print(result)

data = [0]
result = Solution().sortColors(data)
print(result)

data = [2,1]
result = Solution().sortColors(data)
print(result)

data = [0,1]
result = Solution().sortColors(data)
print(result)