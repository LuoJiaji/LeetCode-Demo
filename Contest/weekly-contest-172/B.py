class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        row = 0
        s = s.split(' ')
        for i in s:
            row = max(row, len(i))
        
        rowmax = [0] * row
        # print(row)
        # print(s)
        for i in range(row):  
            curr = 0
            for ind, j in enumerate(s):
                # print(j)
                if len(j) >= i+1:
                    curr = ind
            rowmax[i] = curr
            
        # print(rowmax)

        ans = []
        for i in range(row):
            curr = ''
            for j in range(rowmax[i]+1):
                if len(s[j]) >= i+1:
                    curr += s[j][i]
                else:
                    curr += ' '
            ans.append(curr)
        # print(ans)
        return ans

s = "HOW ARE YOU"
res = Solution().printVertically(s)
print(res)

s = "TO BE OR NOT TO BE"
res = Solution().printVertically(s)
print(res)

s = "CONTEST IS COMING"
res = Solution().printVertically(s)
print(res)
