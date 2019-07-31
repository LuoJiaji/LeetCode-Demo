class Solution(object):
    def getPermutation(self, n, k):

        # divide = 1
        if n == 1:
            return '1'
        result = []
        nums = [i for i in range(1,n+1)]
        # print(nums)
        k = k-1
        for i in range(n-2):
            divide = 1
            for j in range(1,n-i):
                divide *= j
            # print(divide)
            result.append(nums[int(k/divide)])
            
            # print(divide, k, int(k/divide))
            nums.remove(nums[int(k/divide)])
            k = k%divide
            # print(nums,k,divide)
        if k == 0:
            result.append(nums[0])
            # nums.remove(nums[k])
            result.append(nums[1])
        else:
            result.append(nums[1])
            result.append(nums[0])
        # print(result)

        return ''.join([str(i) for i in result])

result = Solution().getPermutation(3, 3)
print(result)
result = Solution().getPermutation(3, 6)
print(result)
result = Solution().getPermutation(4, 9)
print(result)

result = Solution().getPermutation(1, 1)
print(result)
result = Solution().getPermutation(9, 94626)
print(result)




class Solution1(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        flag = [False] * n 
        result = []
        self.PermutationRecu(result, n, flag, [])
        # print(result)
        # print(''.join([str(i) for i in result[k-1]]))
        return ''.join([str(i) for i in result[k-1]])

    def PermutationRecu(self, result, n, flag, curr):
        if False not in flag:
            # print(curr)
            result.append(list(curr))
            return result
        for i in range(n):
            if flag[i] == False:
                curr.append(i+1)
                flag[i] = True
                self.PermutationRecu(result, n, flag, curr)
                curr.pop()
                flag[i] = False



result = Solution1().getPermutation(3, 3)
print(result)
result = Solution1().getPermutation(4, 9)
print(result)
result = Solution1().getPermutation(9, 94626)
print(result)