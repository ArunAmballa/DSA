# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        def diameter(root):
            nonlocal maxDiameter
            if root==None:
                return 0
            leftHeight=diameter(root.left)
            rightHeight=diameter(root.right)
            maxDiameter=max(maxDiameter,leftHeight+rightHeight)
            return max(leftHeight,rightHeight)+1
        maxDiameter=0
        diameter(root)
        return maxDiameter
        