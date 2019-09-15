class Solution(object):

    def max_child(self ,arr):
        result = arr[0]
        sum = arr[0]
        x = 0
        for i in range(1, len(arr)):
            if sum > 0:
                sum += arr[i]
            else:
                sum = arr[i]
                x = i
            if sum > result:
                result = sum
                y = i
        return result

    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """ 
        sub_res = self.max_child(arr)
        sub_res2 = self.max_child(arr+arr)
        sub_sum = sum(arr)
        # print(sub_res, sub_res2, sub_sum)
        # print('sub_res', sub_res, 'k:', k)

        if sub_res2 > sub_res and sub_sum > 0:
            ans = sub_res + (sub_res2-sub_res)*(k-1)
            return ans%(1000000000+7)

        if sub_res < 0:
            ans = 0

        if k == 1 and sub_res >=0:
            ans = sub_res

        if k >= 2:
            # sub_res2 = self.max_child(arr+arr) 
            ans = max(sub_res, sub_res2, 0)
            # print('k>=2:', sub_res2)

        if sub_sum*k > sub_res:
            ans = sum(arr)*k
            # print(ans)
            # return ans

        if sub_sum <= 0 and k >= 2:
            ans = max(sub_res, sub_res2, 0)
        
        # print('ans:',ans)
        return ans%(1000000000+7)



arr = [1,2]
k = 3
res = Solution().kConcatenationMaxSum(arr, k)
print(res)

arr = [1,-2,1]
k = 5
res = Solution().kConcatenationMaxSum(arr, k)
print(res)

arr = [-1,-2]
k = 7
res = Solution().kConcatenationMaxSum(arr, k)
print(res)
