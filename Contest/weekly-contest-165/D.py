class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        sp = []

        l = len(s)

        i = 0
        while i < l:
            for j in range(i+1, l):
                start = i; end = j
                flag = False
                while start < end:
                    if s[start] != s[end]:
                        break
                    start += 1
                    end += 1
                flag = True
                break

            if flag:
                sp.append(s[start:end+1])
                i = end
            else:
                sp.append(s[start])
                i += 1

            print(sp)

    

s = "aabbc"; k = 3
res = Solution().palindromePartition(s,k)
print(res)


