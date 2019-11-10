class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        l = len(mat)
        # print(l)

        for i in mat[0]:
            flag = 1
            for j in range(l):
                if i not in  mat[j]:
                    flag = 0 
                    break
            if flag == 1:
                return i
        return -1





        # return 0


mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
res = Solution().smallestCommonElement(mat)
print(res)