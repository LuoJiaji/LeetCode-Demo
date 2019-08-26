# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p == None and q == None:
            return True
        elif p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

data1 = TreeNode(1)
data1.left = TreeNode(2)
data1.right = TreeNode(3)
data2 = TreeNode(1)
data2.left = TreeNode(2)
data2.right = TreeNode(3)

result = Solution().isSameTree(data2, data2)
print(result)
