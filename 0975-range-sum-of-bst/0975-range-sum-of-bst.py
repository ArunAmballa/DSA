# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root==None:
            return 0
        def helper(root,low,high):
            nonlocal checkSum
            if root==None:
                return 0
            if root.val>=low and root.val<=high:
                checkSum=checkSum+root.val
                helper(root.left,low,high)
                helper(root.right,low,high)
            if root.val<low:
                helper(root.right,low,high)
            if root.val>high:
                helper(root.left,low,high)
        checkSum=0
        helper(root,low,high)
        return checkSum
        