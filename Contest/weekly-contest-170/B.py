class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        curr = [arr[0]]
        l = len(arr)
        for i in range(1, l):
            curr.append(curr[i-1] ^ arr[i])
        # print(curr)
        for l,r in queries:
            if l == 0:
                ans.append(curr[r])
            else:
                ans.append(curr[l-1] ^ curr[r])
        return ans
  

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
res = Solution().xorQueries(arr, queries)
print(res)

arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]
res = Solution().xorQueries(arr, queries)
print(res)