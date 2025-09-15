# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root, result)
        return result

    # Tested python recurrsion variable scope and learned that mutable objects
    # are passed in as memory references to the original object!
    def traversal(self, root, test) -> List[int]:
        if root:
            test.append(root.val)
            self.traversal(root.left, test)
            self.traversal(root.right, test)