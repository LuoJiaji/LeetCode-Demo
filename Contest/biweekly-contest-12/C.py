class Solution:
    def treeDiameter(self, edges):
        def bfs(start):
            # dist = [-1 for _ in dist]
            que = []
            que.append(start)
            dist[start] = 0
            while que != []:   
                p = que[-1]
                del que[-1]              
                for i in E[p]:
                    if dist[i] == -1:
                        dist[i] = dist[p] + 1
                        que.append(i)

        p = []
        for i,j in edges:
            p.append(i)
            p.append(j)

        E = [[] for _ in range(max(p)+1)]
        dist = [-1 for _ in range(max(p) + 1)]

        for i,j in edges:
            E[i].append(j)
            E[j].append(i)

        bfs(0)
        # print(dist)
        p = dist.index(max(dist))
        dist = [-1 for _ in dist]
        bfs(p)
        # print(dist)
        # print(max(dist))
        return max(dist)

# edges = [[0,1],[0,2]]
# res = Solution().treeDiameter(edges)
# print(res)

# edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# res = Solution().treeDiameter(edges)
# print(res)

edges = [[0,1],[1,2],[0,3],[3,4],[2,5],[3,6]]
res = Solution().treeDiameter(edges)
print(res)

edges = [[0,1],[0,2],[1,3],[2,4],[0,5],[3,6],[1,7],[6,8]]
res = Solution().treeDiameter(edges)
print(res)

edges = [[0,1],[1,2],[2,3],[2,4],[0,5],[1,6],[2,7],[6,8],[8,9]]
res = Solution().treeDiameter(edges)
print(res)
