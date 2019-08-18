class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        # n = n-1
        if n < 3:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i] == True:
                # is_prime[2*i :n : i] = [False]*len(is_prime[2*i :n :i])
                is_prime[i*i :n : i] = [False]*len(is_prime[i*i :n :i])
        print(is_prime)
        print(sum(is_prime))

result = Solution().countPrimes(10)
print(result)


# result = Solution().countPrimes(2)
# print(result)