class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        self.ans = 0
        tree = {}

        for i in range(n):
            tree[i] = []
        # print(tree)
        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)
        # print(tree)

        def dfs(n, curr_time):
            if tree[n] == []:
                self.ans = max(self.ans, curr_time)
            for i in tree[n]:
                dfs(i, curr_time + informTime[n])
        
        dfs(headID, 0)
        # print(self.ans)
        return self.ans
                
n = 1
headID = 0
manager = [-1]
informTime = [0]
res = Solution().numOfMinutes(n, headID, manager, informTime)
print(res)

n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
res = Solution().numOfMinutes(n, headID, manager, informTime)
print(res)

n = 7
headID = 6
manager = [1,2,3,4,5,6,-1]
informTime = [0,6,5,4,3,2,1]
res = Solution().numOfMinutes(n, headID, manager, informTime)
print(res)

n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
res = Solution().numOfMinutes(n, headID, manager, informTime)
print(res)

n = 4
headID = 2
manager = [3,3,-1,2]
informTime = [0,0,162,914]
res = Solution().numOfMinutes(n, headID, manager, informTime)
print(res)

n = 10
headID = 3
manager = [8,9,8,-1,7,1,2,0,3,0]
informTime = [224,943,160,909,0,0,0,643,867,722]
res = Solution().numOfMinutes(n, headID, manager, informTime)
print(res)