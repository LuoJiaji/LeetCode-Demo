class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = {'a':['e'], 'e':['a', 'i'], 'i':['a', 'e', 'o', 'u'], 'o':['i', 'u'], 'u':['a']}
        count = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
        curr = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        for _ in range(n-1):
            for i in m:
                for j in m[i]:
                    curr[j] += count[i]

            for i in  m:
                count[i] = curr[i]
                curr[i] = 0
        
        res = 0
        for i in m:
            res += count[i]
        return res%(1000000007)

        # print(count)

        # print(alpha)
        # print(m)
        # print(count)
        
n = 2
res = Solution().countVowelPermutation(n)
print(res)

n = 5
res = Solution().countVowelPermutation(n)
print(res)

n = 144
res = Solution().countVowelPermutation(n)
print(res)