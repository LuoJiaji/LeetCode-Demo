class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        i = 0 
        begin = 0
        end = 0
        mid = 0
        l = len(arr)
        counter = 0
        ans = min(arr)
        # print('ans:', ans)
        # while i < l:
        for i in range(l):
            if arr[i] >= 0 :
                end = i
            else:
                
                end = i
                counter += 1
            
                if counter > 1:
                    # print(arr[begin: end], begin, end, mid)
                    s = arr[begin: end]
                    if len(s) > 1:
                        tmp = sum(s) - min(s)
                        ans = max(ans, tmp)
                    else:
                        tmp = sum(s)
                        ans = max(ans, tmp)
                    # print(ans)
                    begin = mid + 1
                    # begin = i 
                    end = i
                    counter = 1
                mid = end

        # print(arr[begin: end+1], begin, end, mid)
        s = arr[begin: end+1]
        if len(s) > 1:
            tmp = sum(s) - min(s)
            ans = max(ans, tmp)
        else:
            tmp = sum(s)
            ans = max(ans, tmp)
        # tmp = sum(s) - min(s)
        # ans = max(ans, tmp)
        # print(ans)

        return ans


arr = [1,-2,0,3]
result = Solution().maximumSum(arr)
print(result)

arr = [1,-2,-2,3]
result = Solution().maximumSum(arr)
print(result)

arr = [-1,-1,-1,-1]
result = Solution().maximumSum(arr)
print(result)

arr = [1,-2,0,3,-1, 2, 3]
result = Solution().maximumSum(arr)
print(result)
