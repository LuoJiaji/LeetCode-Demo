class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dict_dna = {}
        result = []
        for i in range(len(s)-9):
            # print(s[i:i+10])
            curr = s[i:i+10]
            if curr in dict_dna:
                dict_dna[curr] += 1
            else:
                dict_dna[curr] = 1

            if dict_dna[curr] > 1 and curr not in result:
                result.append(curr)
            
        # print(result)
        return result

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
result = Solution().findRepeatedDnaSequences(s)
print(result)
