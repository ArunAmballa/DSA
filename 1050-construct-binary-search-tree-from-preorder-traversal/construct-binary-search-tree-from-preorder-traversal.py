# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        def helper(preorder,lo,up):
            nonlocal index
            if index>=len(preorder) or preorder[index]<lo or preorder[index]>up:
                return None
            root=TreeNode(preorder[index])
            index=index+1
            root.left=helper(preorder,lo,root.val)
            root.right=helper(preorder,root.val,up)
            return root

        index=0
        return helper(preorder,-math.inf,math.inf)
        