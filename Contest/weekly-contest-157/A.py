class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        cnt = {}
        for i in chips:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        
        # print(cnt)
        res = float('inf')
        for i in cnt:
            ans = 0
            for j in cnt:
                ans += (abs(i-j)%2)*cnt[j]
            # print(ans)
            res = min(res, ans)

        return res





chips = [1,2,3]
res = Solution().minCostToMoveChips(chips)
print(res)

chips = [2,2,2,3,3]
res = Solution().minCostToMoveChips(chips)
print(res)