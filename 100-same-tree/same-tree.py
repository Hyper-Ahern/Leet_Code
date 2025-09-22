# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        # If both initial nodes are empty, they are the same
        if not p and not q:
            return True

        # If p and q exist AND their values at the node in question are the same, it will
        # reccursively return true. If this is untrue at any point, it will skip the if 
        # statement and return false: *** (False AND True) = False ***
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False
