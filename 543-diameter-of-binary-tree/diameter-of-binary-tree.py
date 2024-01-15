# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root==None:
            return 0
        left=self.height(root.left)
        right=self.height(root.right)
        return max(left,right)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        def diameter(root):
            nonlocal maxHeight
            if root==None:
                return 0
            leftHeight=self.height(root.left)
            rightHeight=self.height(root.right)
            maxHeight=max(maxHeight,leftHeight+rightHeight)
            diameter(root.left)
            diameter(root.right)
            return maxHeight
        maxHeight=0
        return diameter(root)
        