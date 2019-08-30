class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        res = abs(C-A) * abs(D-B) + abs(G-E) * abs(H-F)

        if A >= G or E >= C or B >= H or F >= D :
            return res
        
        res -= abs(max(A,E) - min(C,G)) * abs(max(B,F) - min(H, D))
        return res
        
        
        

result = Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
print(result)


result = Solution().computeArea(-2, -2, 2, 2, -4, 3, -3, 4)
print(result)
