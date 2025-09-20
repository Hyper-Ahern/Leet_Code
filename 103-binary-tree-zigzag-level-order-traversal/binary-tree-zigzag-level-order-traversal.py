# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        # make a queue, append the root, make a return result, and create a switch that 
        # determines whether we pop the queue left or right to create a zigzag
        q = collections.deque()
        result = []
        left_to_right = True

        if root:
            q.append(root)

        # While there is something in the q, refresh the level and get new queue length
        while q:
            level = []
            q_length = len(q)

            # For each item on the level, check if we are printing left to right or in reverse,
            # grab the node, store the children in the queue then add the value to the level list
            for i in range(q_length):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # If level has nothing in it, we don't want to add null sets so skip it. Also,
            # we will append left to right or in reverse depending on the left_to_right switch
            if level and left_to_right:
                result.append(level)
            elif level and not left_to_right:
                level = list(reversed(level))
                result.append(level)

            # Set the zigzag to the opposite by using a not opperator to flip it
            left_to_right = not left_to_right
        
        return result