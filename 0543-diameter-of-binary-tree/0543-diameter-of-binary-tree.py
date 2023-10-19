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
        return max(lh,rh)+1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        leftDiameter=self.diameterOfBinaryTree(root.left)
        rightDiameter=self.diameterOfBinaryTree(root.right)
        rootDiameter=self.height(root.left)+self.height(root.right)
        return max(rootDiameter,max(leftDiameter,rightDiameter))


        