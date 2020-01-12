class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        net = [set()]
        res = 0
        net[0].add(connections[0][0])
        net[0].add(connections[0][1])
        l = len(connections)
        for i in range(1,l):
            x = connections[i][0]
            y = connections[i][1]
            
            nset = len(net)
            a = -1
            b = -1
            for ind in range(nset):
                if x in net[ind]:
                    a = ind
                if y in net[ind]:
                    b = ind
            if a == -1 and b == -1:
                new_net = set()
                new_net.add(x)
                new_net.add(y)
                net.append(new_net)
            elif a == -1 and b != -1:
                net[b].add(x)
                # res += 1
            elif a != -1 and b == -1:
                net[a].add(y)
                # res += 1
            elif a != -1 and b != -1 and a != b:
                net[a] |= net[b]
                net.remove(net[b])
            elif a != -1 and b != -1 and a == b:
                res += 1

        # print(net)
        cnt = [len(i) for i in net]
        # print(cnt)
        cnt = sum(cnt)
        # print(cnt)
        need = len(net) + n - cnt - 1 
        print(net, res, need)
        if res >= need:
            return need
        else:
            return -1
        # print(net, res)


n = 4
connections = [[0,1],[0,2],[1,2]]
res = Solution().makeConnected(n, connections)
print(res)

n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
res = Solution().makeConnected(n, connections)
print(res)

n = 6
connections = [[0,1],[0,2],[0,3],[1,2]]
res = Solution().makeConnected(n, connections)
print(res)

n = 5
connections = [[0,1],[0,2],[3,4],[2,3]]
res = Solution().makeConnected(n, connections)
print(res)

n = 100
connections = [[17,51],[33,83],[53,62],[25,34],[35,90],[29,41],[14,53],[40,84],[41,64],[13,68],[44,85],[57,58],[50,74],[20,69],[15,62],[25,88],[4,56],[37,39],[30,62],[69,79],[33,85],[24,83],[35,77],[2,73],[6,28],[46,98],[11,82],[29,72],[67,71],[12,49],[42,56],[56,65],[40,70],[24,64],[29,51],[20,27],[45,88],[58,92],[60,99],[33,46],[19,69],[33,89],[54,82],[16,50],[35,73],[19,45],[19,72],[1,79],[27,80],[22,41],[52,61],[50,85],[27,45],[4,84],[11,96],[0,99],[29,94],[9,19],[66,99],[20,39],[16,85],[12,27],[16,67],[61,80],[67,83],[16,17],[24,27],[16,25],[41,79],[51,95],[46,47],[27,51],[31,44],[0,69],[61,63],[33,95],[17,88],[70,87],[40,42],[21,42],[67,77],[33,65],[3,25],[39,83],[34,40],[15,79],[30,90],[58,95],[45,56],[37,48],[24,91],[31,93],[83,90],[17,86],[61,65],[15,48],[34,56],[12,26],[39,98],[1,48],[21,76],[72,96],[30,69],[46,80],[6,29],[29,81],[22,77],[85,90],[79,83],[6,26],[33,57],[3,65],[63,84],[77,94],[26,90],[64,77],[0,3],[27,97],[66,89],[18,77],[27,43]]
res = Solution().makeConnected(n, connections)
print(res)

# a = set()
# a.add(1)
# b = set()
# b.add(10)
# a |= b
# print(a)
# c = [a, b]
# print(c)
# c.remove(b)
# print(c)