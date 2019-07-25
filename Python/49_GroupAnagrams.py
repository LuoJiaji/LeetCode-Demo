# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 16:55:08 2019

@author: Bllue
"""

# solution1 超时了，因为用了双循环，
# solution2 把数据结构改成字典类型
class Solution1(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        flag = [False] * len(strs)
        result = []
        simlar = []
        i = 0
        while False in flag and i < len(strs):
            simlar = []
            if flag[i] == False:
                simlar.append(strs[i])
                
                for j in range(i+1, len(strs)):
                    if sorted(strs[j]) == sorted(strs[i]):
                        simlar.append(strs[j])
                        flag[j] = True
            
#            print(simlar)
            
            if len(simlar) != 0:
                result += [simlar]
            i += 1
            
        return result
    
    
class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        dic = {}
        for i in range(len(strs)):
            tmp = ('').join(sorted(strs[i]))
#            print(tmp)
            if tmp in dic:
                dic[tmp].append(strs[i])
            else:
                dic[tmp] = []
                dic[tmp].append(strs[i])
#        print(dic)
#        print(len(dic))
        for i in dic:
#            print(i,dic[i])
            result.append(dic[i])
#        print(result)
        return result
            
#        return result    
    
data = ["ett","ee","tan","ate","nat","bat"]
result = Solution2().groupAnagrams(data)
print(result)

