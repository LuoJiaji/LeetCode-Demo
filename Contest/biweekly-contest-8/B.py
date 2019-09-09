class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        ans = []

        data = [i.split(' ') for i in phrases]
        # print(data)
        
        for i in range(len(data)):
            for j in range(len(data)):
                
                if i != j and data[i][-1] == data[j][0]:
                    tmp = ' '.join(data[i] + data[j][1:])
                    # print(tmp)
                    if tmp not in ans:
                        ans.append(tmp) 
        ans.sort()
        return ans
        

phrases = ["writing code","code rocks"]
result = Solution().beforeAndAfterPuzzles(phrases)
print(result)

phrases = ["mission statement",
                "a quick bite to eat",
                "a chip off the old block",
                "chocolate bar",
                "mission impossible",
                "a man on a mission",
                "block party",
                "eat my words",
                "bar of soap"]
result = Solution().beforeAndAfterPuzzles(phrases)
print(result)

phrases = ["a","b","a"]
result = Solution().beforeAndAfterPuzzles(phrases)
print(result)
