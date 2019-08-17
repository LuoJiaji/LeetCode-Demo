class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        re = 0
        tmp = []

        if triangle == []:
            return []
        
        if len(triangle) == 1:
            return triangle[0][0]

        tmp.append(triangle[1][0] + triangle[0][0])
        tmp.append(triangle[1][1] + triangle[0][0])
        
        if len(triangle) == 2:
            return min(tmp)

        # print(tmp)   
        for i in range(2,len(triangle)):
            # print(triangle[i],i)
            pre = tmp
            tmp = []
            re = 0
            tmp.append(pre[0] + triangle[i][0])
            for j in range(1,i):
                # print(i,j)
                # print(triangle[i][j])
                tmp.append(min(pre[j-1], pre[j]) + triangle[i][j])
            tmp.append(pre[-1] + triangle[i][-1])

            pre = tmp
            # print(tmp)
            # print(min(tmp))
        return min(tmp)

 
data = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]]
result = Solution().minimumTotal(data)
print(result)

data = [
     [2],
    [3,4]]
result = Solution().minimumTotal(data)
print(result)

data = [
     [2]]
result = Solution().minimumTotal(data)
print(result)

data = []
result = Solution().minimumTotal(data)
print(result)