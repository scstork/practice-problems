# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    """
    Given the root of a binary tree, return its maximum depth.
    
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    """

    def maxDepth(self, root: TreeNode) -> int:
        return self.recurse_down(root, 0)
        
    def recurse_down(self, root: TreeNode, current_max: int):
        if root is None:
            return current_max
        current_max +=1
        left_max = current_max
        right_max = current_max
        if root.left:
            left_max = self.recurse_down(root.left, current_max)
        if root.right:
            right_max = self.recurse_down(root.right, current_max)
        current_max = max(current_max, left_max, right_max)
        return current_max