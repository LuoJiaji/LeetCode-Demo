class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans = 0
        while a >0 or b > 0 or c > 0:
            tmp_a = a % 2
            tmp_b = b % 2
            tmp_c = c % 2
            # print(tmp_a, tmp_b, tmp_c)
            a = int(a/2)
            b = int(b/2)
            c = int(c/2)
            if tmp_c == 1:
                if tmp_a == 0 and tmp_b == 0:
                    ans += 1
            if tmp_c == 0:
                if tmp_a == 1:
                    ans += 1
                if tmp_b == 1:
                    ans += 1
        return ans

                            

a = 2
b = 6
c = 5
res = Solution().minFlips(a, b, c)
print(res)

a = 4
b = 2
c = 7
res = Solution().minFlips(a, b, c)
print(res)

a = 1
b = 2
c = 3
res = Solution().minFlips(a, b, c)
print(res)

res = Solution().minFlips(8, 3, 5)
print(res)