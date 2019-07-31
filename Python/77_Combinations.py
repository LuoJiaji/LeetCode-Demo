class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        flag = [False]*n
        nums = [i+1 for i in range(n)]
        result = []
        self.combineRecu(flag, [], k, nums, 0, result)
        # print(result)
        return result

    def combineRecu(self, flag, curr, k, nums, start, result):
        # print(start)
        if len(curr) == k:
            # print(curr)
            result.append(list(curr))
            return result
        
        for i in range(start, len(nums)):
            if flag[i] == False:
                curr.append(nums[i])
                flag[i] = True
                self.combineRecu(flag, curr, k, nums, i, result)
                curr.pop()
                flag[i] = False
        

result = Solution().combine(4,4)
print(result)

