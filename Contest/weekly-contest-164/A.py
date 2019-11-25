class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        l = len(points)
        for i in range(1,l):
            ans += min(abs(points[i-1][0]-points[i][0]), abs(points[i-1][1]-points[i][1])) + abs(abs(points[i-1][0]-points[i][0])- abs(points[i-1][1]-points[i][1]))

        # print(ans)
        return ans

points = [[1,1],[3,4],[-1,0]]
res = Solution().minTimeToVisitAllPoints(points)