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
        if lh==-1:
            return -1
        rh=self.height(root.right)
        if rh==-1:
            return -1
        if (abs(lh-rh))>1:
            return -1
        return max(lh,rh)+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        ans=self.height(root)
        return False if ans==-1 else True
        