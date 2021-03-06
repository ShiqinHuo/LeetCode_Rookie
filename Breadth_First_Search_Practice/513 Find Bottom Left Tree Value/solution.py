# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        current_row = [root]
        result = root.val
        while current_row:
            next_row = []
            for node in current_row:
                if (node.left):
                    next_row.append(node.left)
                if (node.right):
                    next_row.append(node.right)
            result = current_row[0].val
            current_row = next_row

        return result
