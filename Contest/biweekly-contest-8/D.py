class Solution(object):
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        """
        :type width: int
        :type height: int
        :type sideLength: int
        :type maxOnes: int
        :rtype: int
        """
        cnt = []

        for i in range(sideLength):
            for j in range(sideLength):
                tmp = 1 if i < int(width % sideLength) else 0
                w = int(width / sideLength) + tmp
                tmp = 1 if j < int(height % sideLength) else 0
                h = int(height / sideLength) + tmp
                cnt.append(w*h)
        # print(cnt)
        ans = 0
        for i in range(maxOnes):
            tmp = max(cnt)
            ans += tmp
            cnt.remove(tmp)
        
        # print(ans)
        return ans

width = 3
height = 3
sideLength = 2
maxOnes = 1
result = Solution().maximumNumberOfOnes(width, height, sideLength, maxOnes)
print(result)

width = 3
height = 3
sideLength = 2
maxOnes = 2
result = Solution().maximumNumberOfOnes(width, height, sideLength, maxOnes)
print(result)
