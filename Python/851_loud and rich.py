import copy 
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        bigger = {}
        for i in richer:
            if i[1] not in bigger:
                bigger[i[1]] = []
                bigger[i[1]].append(i[0])
            else:
                bigger[i[1]].append(i[0])
        # print(bigger)

        l = len(quiet)
        ans = []
        for i in range(l):
            tmp = [quiet[i]]
            if i in bigger:
                que = copy.deepcopy(bigger[i])
                while que:
                    # print(i,que,que[0], que[0] in bigger, bigger)
                    tmp.append(quiet[que[0]])
                    if que[0] in bigger:
                        que += bigger[que[0]]
                    del que[0]
            # print(tmp)
            
            ans.append(quiet.index(min(tmp)))
        # print(ans)
        return ans

from collections import defaultdict


class Solution:
    def loudAndRich(self, richer, quiet):
        graph = defaultdict(list)

        richest = set()

        for rich, rich_man in richer:
            graph[rich].append(rich_man)
            richest.add(rich)
            if rich_man in richest:
                richest.remove(rich_man)
        
        print(graph, richest)

        ans = list(range(len(quiet)))

        temp = richest

        while temp:
            next_temp = set()
            for rich in temp:
                for poor in graph[rich]:
                    if quiet[ans[rich]] < quiet[ans[poor]]:
                        ans[poor] = ans[rich]
                    next_temp.add(poor)
            temp = next_temp

        return ans

richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
res = Solution().loudAndRich(richer, quiet)
print(res)
