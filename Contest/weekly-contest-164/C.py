class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products = sorted(products)
        # print(products)
        l = len(searchWord)
        ans = []
        for i in range(1,l+1):
            tmp = []
            for p in products:
                if p[0:i] == searchWord[0:i]:
                    tmp.append(p)
                if len(tmp) >= 3:
                    break
            ans.append(tmp)
        return ans


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
res = Solution().suggestedProducts(products, searchWord)
print(res)

products = ["havana"]
searchWord = "havana"
res = Solution().suggestedProducts(products, searchWord)
print(res)

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"
res = Solution().suggestedProducts(products, searchWord)
print(res)

products = ["havana"]
searchWord = "tatiana"
res = Solution().suggestedProducts(products, searchWord)
print(res)