class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        from collections import Counter
        # fri_k = []
        visited = [id]
        curr = friends[id]
        visited += curr
        # print(visited)
        # print(curr)
        for _ in range(level - 1):
            curr_new = []
            for f in curr:
                for n in friends[f]:
                    if n not in visited:
                        curr_new.append(n)
                        visited.append(n)
                # print(curr_new)
            curr = curr_new
        # print(curr)

        l = []
        for i in curr:
            l += watchedVideos[i]
        # print(l)
        # print(dict(Counter(l)))
        ans = dict(Counter(l))
        ans = sorted(ans.items(), key=lambda item: item[1])
        # print(ans)
        fre = 1
        # res = [k for k,i in ans]
        curr = []
        res = []
        for k,i in ans:
            if i == fre:
                curr.append(k)
            else:
                fre = i
                res += sorted(curr)
                curr = []
                curr.append(k)
        res += sorted(curr)
        # print(res)
        return res

watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 1
res = Solution().watchedVideosByFriends(watchedVideos, friends, id, level)
print(res)

watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 2
res = Solution().watchedVideosByFriends(watchedVideos, friends, id, level)
print(res)


watchedVideos = [["bjwtssmu"],["aygr","mqls"],["vrtxa","zxqzeqy","nbpl","qnpl"],["r","otazhu","rsf"],["bvcca","ayyihidz","ljc","fiq","viu"]]
friends = [[3,2,1,4],[0,4],[4,0],[0,4],[2,3,1,0]]
id = 3
level = 1
res = Solution().watchedVideosByFriends(watchedVideos, friends, id, level)
print(res)
# print(sorted(res))

# tmp = {'A':2, 'B':1, 'C':2}
# print(sorted(tmp.items(), key=lambda item: item[1]))