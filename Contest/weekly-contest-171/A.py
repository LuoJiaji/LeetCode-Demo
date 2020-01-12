class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def isnozero(num):
            for i in str(num):
                if i == '0':
                    return False
            return True

        a = 1
        b = n-a
        while True:
            if isnozero(a) and isnozero(b):
                return [a,b]
            else:
                a += 1
                b = n-a


res = Solution().getNoZeroIntegers(2)
print(res)

res = Solution().getNoZeroIntegers(11)
print(res)

res = Solution().getNoZeroIntegers(10000)
print(res)

res = Solution().getNoZeroIntegers(69)
print(res)

res = Solution().getNoZeroIntegers(1010)
print(res)