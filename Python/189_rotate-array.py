class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # print(nums[-k:])
        # print(nums[:-k])
        for _ in range(k%len(nums)):
            nums.insert(0, nums[-1])
            nums.pop()
        # nums = result
        print(nums)
        # return result


data = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(data,k)
print(data)

data =[-1,-100,3,99] 
k = 2
Solution().rotate(data,k)
print(data)

data =[-1,-100] 
k = 3
Solution().rotate(data,k)
print(data)

a = [1,2,3,4]
a.insert(0,10,10,10)
print(a)