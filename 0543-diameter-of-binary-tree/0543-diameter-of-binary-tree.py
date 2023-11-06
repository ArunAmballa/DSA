# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None or (root.left==None and root.right==None):
            return 0
        def helper(root):
            nonlocal diameter
            if root==None:
                return 0
            leftHeight=helper(root.left)
            rightHeight=helper(root.right)
            diameter=max(diameter,leftHeight+rightHeight)
            return max(leftHeight,rightHeight)+1
        diameter=0
        helper(root)
        return diameter
        
        