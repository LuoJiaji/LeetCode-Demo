class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ln = len(str(low))
        hn = len(str(high))
        ans = []
        for n in range(ln, hn + 1):
            # print(n)
            for i in range(1, 11-n):
                num = ''.join([str(i) for i in range(i, i+n)])
                num = int(num)
                # print(n,i,num)
                if num > high:
                    break
                if num >= low:
                    ans.append(num)
        return ans


low = 100
high = 300
res = Solution().sequentialDigits(low, high)
print(res)

low = 1000
high = 13000
res = Solution().sequentialDigits(low, high)
print(res)