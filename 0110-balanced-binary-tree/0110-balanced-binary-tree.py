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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        isLeft=self.isBalanced(root.left)
        isRight=self.isBalanced(root.right)
        isRoot=True if (abs(self.height(root.left)-self.height(root.right))<=1) else False
        return (isLeft and isRight and isRoot)