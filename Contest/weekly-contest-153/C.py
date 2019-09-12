class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        f = [0]*n
        g = [0]*n

        for i in range(n):
            f[i] = arr[i]
            if i > 0 and f[i-1] > 0:
                f[i] += f[i-1]

        for i in reversed(range(n)):
            g[i] = arr[i]
            if i < n-1 and g[i+1] > 0:
                g[i] += g[i+1]
        
        # print(f,g)
        ans = f[0]
        for i in range(n):
            ans = max(ans, max(f[i], g[i]))
            if i+1 < n:
                ans = max(ans, f[i] + g[i+1])
            if i+2 < n:
                ans = max(ans, f[i] + g[i+2])
            # print(ans,i,n)

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
