class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        dst = []
        for i in range(len(s)):
            dst.append(abs(ord(s[i]) - ord(t[i])))
        print(dst)
        
        l = dst[0]
        begin = 0
        end = 0
        res = 0
        while end <= len(dst)-1:
            print(begin, end, res, l)

            if l <= maxCost :
                res = max(res, end - begin + 1)

            if (l <= maxCost or begin == end)  and end < len(dst) - 1:
                end += 1
                l += dst[end]
                continue
                # if l <= cost:
                #     res = max(res, end - begin + 1)
            if l > maxCost and begin < end:
                # if begin != len(dst) -1:
                l -= dst[begin]
                begin += 1
                continue

            if end == len(dst) -1 and begin < end:
                l -= dst[begin]
                begin += 1
                continue

            if (begin == end or l < cost) and end == len(dst) -1 :
                break
            # print(begin, end, res)
            
        # print(res)
        return res

# s = "abcd"
# t = "bcdf"
# cost = 3
# res = Solution().equalSubstring(s,t,cost)
# print(res)

# s = "abcd"
# t = "cdef"
# cost = 3
# res = Solution().equalSubstring(s,t,cost)
# print(res)

# s = "abcd"
# t = "acde"
# cost = 0
# res = Solution().equalSubstring(s,t,cost)
# print(res)

s = "krpgjbjjznpzdfy"
t = "nxargkbydxmsgby"
cost = 14
res = Solution().equalSubstring(s,t,cost)
print(res)