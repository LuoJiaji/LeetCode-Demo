class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        n = str(num)
        ans = ''
        flag = 0
        for i in n:
            if i == '6' and flag == 0:
                ans += '9'
                flag = 1
            else:
                ans += i
        return ans




res = Solution().maximum69Number(9669)
print(res)

res = Solution().maximum69Number(9996)
print(res)

res = Solution().maximum69Number(9999)
print(res)