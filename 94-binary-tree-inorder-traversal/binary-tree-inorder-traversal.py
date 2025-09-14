# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):

        # Create a result to return with the data then call the helper function recursively
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, result):

        # If the root is None, Null, etc, skip to the end of the function, else,
        # call this function again on the left -> root -> right nodes until the
        # result is completed.
        if root:
            self.helper(root.left, result)
            result.append(root.val)
            self.helper(root.right, result)