# class Solution(object):
#     def isPossibleDivide(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         # print(len(nums) // k)
#         if len(nums) % k != 0:
#             return False
#         n = len(nums) / k
#         # nums.sort()
#         print(nums)
#         for i in range(int(n)):
#             # curr = nums[0]
#             curr = min(nums)
#             nums.remove(curr)
#             for _ in range(k-1):
#                 curr += 1
#                 if curr in nums:
#                     nums.remove(curr)
#                 else:
#                     return False
#         return True

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # print(len(nums) // k)
        if len(nums) % k != 0:
            return False
        # n = len(nums) / k
        nums.sort()
        # print(nums)
        cnt = {}
        for i in nums:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        # print(cnt)

        for i in nums:
            if cnt[i] == 0:
                continue
            for j in range(k):
                # print(i+j)
                if i+j not in cnt or cnt[i+j] == 0:
                    return False
                cnt[i+j] -= 1
        return True


# nums = [1,2,3,3,4,4,5,6]
# k = 4
# res = Solution().isPossibleDivide(nums, k)
# print(res)

# nums = [3,2,1,2,3,4,3,4,5,9,10,11]
# k = 3
# res = Solution().isPossibleDivide(nums, k)
# print(res)

# nums = [3,3,2,2,1,1]
# k = 3
# res = Solution().isPossibleDivide(nums, k)
# print(res)
# nums = [1,2,3,4]
# k = 3
# res = Solution().isPossibleDivide(nums, k)
# print(res)

nums = [5,6,7,8,9,6,7,8,9,10,11,12,13,14,15,12,13,14,15,19]
k = 5
res = Solution().isPossibleDivide(nums, k)
print(res)