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
            nonlocal valSum
            if root==None:
                return 
            if root.val>=low and root.val<=high:
                valSum=valSum+root.val
                helper(root.left,low,high)
                helper(root.right,low,high)
            else:
                if root.val>high:
                    helper(root.left,low,high)
                else:
                    helper(root.right,low,high)
        valSum=0
        helper(root,low,high)
        return valSum
        