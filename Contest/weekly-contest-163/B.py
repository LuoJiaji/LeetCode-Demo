# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.l = []
        
        def rest(node, n):
            node.val = n
            self.l.append(n)
            if node.left != None:
                rest(node.left, 2*n + 1)
            if node.right  != None:
                rest(node.right, 2*n + 2)
            
        root.val = 0
        num = root.val
        self.l.append(num)
        if root.left != None:
            rest(root.left, 2*num+1)
        if root.right  != None:
            rest(root.right, 2*num+2)
        self.root = root
        
        # print(self.l)
        
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
#         self.ans = False
#         def dfs(node, target):
#             if node.val == target:
#                 self.ans = True
#             else :
#                 if node.left != None:
#                     dfs(node.left, target)
#                 if node.right  != None:
#                     dfs(node.right, target) 
            
            
#         if self.root.val == target:
#             self.ans = True
#         else :
#             if self.root.left != None:
#                 dfs(self.root.left, target)
#             if self.root.right  != None:
#                 dfs(self.root.right, target)
        if target in self.l:
            return True
        else:
            return False
        # return self.ans
            


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)