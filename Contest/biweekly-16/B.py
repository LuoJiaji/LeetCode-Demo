class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = sum(arr)
        mid = int((left + right)/2)
        if len(arr) > target:
            return 0
        # print(mid)
        ans_sum = abs(sum(arr) - target)
        ans = mid
        while  right - left > 1:
            mid = int((left + right)/2)
            curr = [i if i <= mid else mid for i in arr]
            tmp = sum(curr)
            if tmp > target:
                right = mid
            else:
                left = mid 
            
            if  abs(tmp - target) == ans_sum:
                ans = min(ans, mid)

            if abs(tmp - target) < ans_sum:
                ans_sum = abs(tmp - target)
                ans = mid
        
            # print(left, right, mid,ans_sum ,curr)
        return ans
        
arr = [4,9,3]
target = 10
res = Solution().findBestValue(arr, target)
print(res)

arr = [2,3,5]
target = 10
res = Solution().findBestValue(arr, target)
print(res)

arr = [60864,25176,27249,21296,20204]
target = 56803
res = Solution().findBestValue(arr, target)
print(res)
