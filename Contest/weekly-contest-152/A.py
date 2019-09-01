class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = n+1
        isPre = [0] * n

        l = int(n**0.5)
        for i in range(2,l+1):
            if isPre[i]:
                continue
            isPre[i*i:n:i] = [1] *len(isPre[i*i:n:i])

        counter_Pre = n - sum(isPre) - 2
        counter_noPre = n -1  - counter_Pre

        import math
        # print(counter_Pre, counter_noPre)
        res = (math.factorial(counter_Pre) * math.factorial(counter_noPre))%int(1e9+7)
        # print(res)
        return res

result = Solution().numPrimeArrangements(3)
print(result)
result = Solution().numPrimeArrangements(5)
print(result)
result = Solution().numPrimeArrangements(100)
print(result)
# print(1e9)
# print(10**9)
# print()