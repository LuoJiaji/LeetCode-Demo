class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # print(n)
        # print(n[::-1])
        # rev = n[::-1]
        return int(bin(n)[2:].zfill(32)[::-1],2)

data = 43261596
result = Solution().reverseBits(data)
print(result)

data = 4294967293
result = Solution().reverseBits(data)
print(result)