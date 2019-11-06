class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """

        def check(sweetness, mid):
            s = 0
            count = 0
            for i in sweetness:
                s += i
                if s >= mid:
                    s = 0
                    count += 1
            if count >= K + 1:
                return True
            else:
                return False

        left = 0
        right = sum(sweetness) + 1
        ans = min(sweetness)

        while left < right:
            mid = int((left + right )/2)

            if check(sweetness, mid):
                ans = max(ans, mid) 
                left = mid + 1
            else:
                right = mid 
            
        return ans

sweetness = [1,2,3,4,5,6,7,8,9]
K = 5
res = Solution().maximizeSweetness(sweetness, K)
print(res)

sweetness = [5,6,7,8,9,1,2,3,4]
K = 8
res = Solution().maximizeSweetness(sweetness, K)
print(res)

sweetness = [1,2,2,1,2,2,1,2,2]
K = 2
res = Solution().maximizeSweetness(sweetness, K)
print(res)

sweetness = [19679,20653,68010,3714,54485,548,41366,11201,47138,70768,1050,87246,17114,56157,13235,65363,30444,56929,21969,22308]
K = 0
res = Solution().maximizeSweetness(sweetness, K)
print(res)
