class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        tree = {}
        self.ans = 0
        for i in range(n+1):
            tree[i] = []
        for i,j in edges:
            tree[i].append(j)
            tree[j].append(i)
        # print(tree)
        flag = [0]*(n+1)

        def dfs(node, n, p):
            if n == t and node == target:
                self.ans = p

            if n < t:
                flag[node] = 1
                togo = []
                for i in tree[node]:
                    if flag[i] == 0:
                        togo.append(i)
                if togo == []:
                    dfs(node, n+1, p)
                else:
                    for i in togo:
                        dfs(i, n+1, p * (1.0/len(togo)))
            
        dfs(1, 0, 1)
        # print(self.ans)
        return self.ans



n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 4
res = Solution().frogPosition(n, edges, t, target)
print(res)

n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 1
target = 7
res = Solution().frogPosition(n, edges, t, target)
print(res)

n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 20
target = 6
res = Solution().frogPosition(n, edges, t, target)
print(res)
