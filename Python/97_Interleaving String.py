class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        result = self.isInterleaveRecu(s1, s2, s3, 0, 0, 0)
        return result
    
    def isInterleaveRecu(self, s1, s2, s3, i, j, k):
        if k == len(s3):
            return True
        result = False
        if i < len(s1) and s1[i] == s3[k]:
            result = result or self.isInterleaveRecu(s1, s2, s3, i+1, j, k+1)
        if j < len(s2) and s2[j] == s3[k]:
            result = result or self.isInterleaveRecu(s1, s2, s3, i, j+1, k+1)
        # else:
            # return False
        # print("out of range!!!")
        return result

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

result = Solution().isInterleave(s1, s2, s3)
print(result)
