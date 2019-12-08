class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        
        cnt = {}
        l = len(groupSizes)
        for i in range(l):
            if groupSizes[i] not in cnt:
                cnt[groupSizes[i]] = [i]
            else:
                cnt[groupSizes[i]].append(i)
        # print(cnt)

        ans = []

        for i in cnt:
            # print(i,cnt[i]) 
            j = 0
            while j < len(cnt[i]):
                ans.append(cnt[i][j:j+i])
                j += i
        # print(ans)
        return ans

groupSizes = [3,3,3,3,3,1,3]
res = Solution().groupThePeople(groupSizes)
print(res)

groupSizes = [2,1,3,3,3,2]
res = Solution().groupThePeople(groupSizes)
print(res)
