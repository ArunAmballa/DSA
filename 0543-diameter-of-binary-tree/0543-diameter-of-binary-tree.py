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
        leftAns=self.diameterOfBinaryTree(root.left)
        rightAns=self.diameterOfBinaryTree(root.right)
        currAns=self.height(root.left)+self.height(root.right)
        return max(leftAns,max(rightAns,currAns))

        