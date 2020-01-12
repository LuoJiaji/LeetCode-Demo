# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(root):
            # print(root.val)
            if root.val % 2 == 0:
                if root.left and root.left.left:
                    self.ans += root.left.left.val
                if root.left and root.left.right:
                    self.ans += root.left.right.val
                if root.right and root.right.left:
                    self.ans += root.right.left.val
                if root.right and root.right.right:
                    self.ans += root.right.right.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        return self.ans
            