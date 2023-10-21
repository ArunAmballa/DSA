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
        lh=self.height(root.left)
        rh=self.height(root.right)
        self.diameter=max(self.diameter,lh+rh)
        return max(lh,rh)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.height(root)
        return self.diameter
        