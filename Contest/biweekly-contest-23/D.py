class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        s = sorted(satisfaction)
        # print(s)
        ans = 0
        for i in range(len(s)):
            if s[i] <= 0:
                # print(s[i:])
                subs = s[i:]
                tmp = 0 
                for a,b  in enumerate(subs):
                    tmp += (a+1)*b
                # print(tmp)
                if tmp > ans:
                    ans = tmp

        nneg = []
        for i in satisfaction:
            if i > 0:
                nneg.append(i)

        nneg = sorted(nneg)
        # print(nneg)

        tmp = 0
        for a,b in enumerate(nneg):
            tmp += (a+1)*b

        if ans < tmp:
            ans = tmp
        return ans




            # print()


satisfaction = [-1,-8,0,5,-9]
res = Solution().maxSatisfaction(satisfaction)
print(res)

satisfaction = [4,3,2]
res = Solution().maxSatisfaction(satisfaction)
print(res)

satisfaction = [-1,-4,-5]
res = Solution().maxSatisfaction(satisfaction)
print(res)

satisfaction = [-2,5,-1,0,3,-3]
res = Solution().maxSatisfaction(satisfaction)
print(res)