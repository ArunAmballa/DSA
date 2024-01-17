# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def helper(self,root,lo,hi):
        if root==None:
            return True
        if root.val<=lo or root.val>=hi:
            return False
        return self.helper(root.left,lo,root.val) and self.helper(root.right,root.val,hi)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,-math.inf,math.inf)