# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        # Create a result list, a deque, and append the first node to the deque
        result = []
        q = collections.deque()
        q.append(root)

        # While there is something in the queue, get the nnumber of elements in that 
        # queue, and make a fresh level list
        while q:
            q_length = len(q)
            level = []     

            # for each node in the queue, pop it off the LEFT side, place its value in the level
            # list and its children in the queue. Do this i times for each previous level node
            for i in range(q_length):
                current_node = q.popleft()

                if current_node:
                    level.append(current_node.val)
                    q.append(current_node.left)
                    q.append(current_node.right)

            # To make sure that a null level set is not added, make sure there is something 
            # IN the level list before adding it, otherwise it was null so we skip it
            if level:
                result.append(level)

        return result