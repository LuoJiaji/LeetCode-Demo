# class Solution(object):
#     def palindromePartition(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         sp = []

#         l = len(s)

#         i = 0
#         while i < l:
#             for j in range(i+1, l):
#                 start = i; end = j
#                 flag = False
#                 while start < end:
#                     if s[start] != s[end]:
#                         break
#                     start += 1
#                     end += 1
#                 flag = True
#                 break

#             if flag:
#                 sp.append(s[start:end+1])
#                 i = end
#             else:
#                 sp.append(s[start])
#                 i += 1

#             print(sp)


class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dp = [[-1 for _ in range(150)] for _ in range(150)]

        def clac(s, a, b):
            ret = 0
            for i in range(a, b+1):
                if s[i - 1] != s[b - (i-a) - 1]:
                    ret += 1
            return int(ret/2)

        n = len(s)

        dp[0][0] = 0
        for i in range(n):
            for c in range(k):
                if dp[i][c] == -1:
                    continue
                for j in range(i+1, n+1):
                    cost = clac(s, i+1, j)
                    # print(cost,  dp[j][c+1])
                    if dp[j][c+1] == -1 or dp[j][c+1] > dp[i][c] + cost:
                        dp[j][c+1] = dp[i][c] + cost
    
        return dp[n][k]

s = "abc"; k = 2
res = Solution().palindromePartition(s,k)
print(res)

s = "aabbc"; k = 3
res = Solution().palindromePartition(s,k)
print(res)

s = "leetcode"; k = 8
res = Solution().palindromePartition(s,k)
print(res)
