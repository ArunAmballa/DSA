# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None:
            return None
        if root.left==None and root.right==None:
            return root
        leftTree=self.flatten(root.left)
        rightTree=self.flatten(root.right)
        if leftTree!=None:
            leftTree.right=root.right
            root.right=root.left
            root.left=None
        if rightTree==None:
            return leftTree
        return rightTree
        