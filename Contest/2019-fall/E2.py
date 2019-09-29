class Solution:
     def bonus(self, n, leadership, operations):
        mod = int(1e9 + 7)
        
        tree = {}
        for i in range(n+1):
            tree[i] = []

        for i in leadership:
            tree[i[0]].append(i[1])
        # print(tree)

        money = [0]*(n+1)

        def dfs(n):
            tmp = []
            for i in tree[n]:
                tmp += tree[i]
                tmp += dfs(i)
            tree[n] += tmp
            return tmp

        for i in range(n+1):
            dfs(i)
        # print(tree)

        for i in tree:
            tree[i] = list(set(tree[i]))
        print(tree)

        ans = []
        for i in operations:
            if i[0] == 1:
                money[i[1]] += i[2]

            if i[0] == 2:
                money[i[1]] +=  i[2]
                # print(tree[i[1]])
                for j in tree[i[1]]:
                    # print(j,i[2])
                    money[j] += i[2]
            
            if i[0] == 3:
                s = 0
                s += money[i[1]]
                for i in tree[i[1]]:
                    s += money[i]
                ans.append(s%mod)
            print(money)

        # print(ans)
        return ans

N = 6
leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4]]
operations = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]
res = Solution().bonus(N, leadership, operations)
print(res)

N = 8
leadership = [[1, 2], [1, 6], [2, 3], [2, 5], [1, 4],[3,7],[3,8]]
operations = [[1, 1, 500], [2, 2, 50], [3, 1], [2, 6, 15], [3, 1]]
res = Solution().bonus(N, leadership, operations)
print(res)
