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
        
        def helper(root,lo,hi):
            nonlocal ans
            if root==None:
                return None
            if root.val>=lo and root.val<=hi:
                ans=ans+root.val
                helper(root.left,lo,hi)
                helper(root.right,lo,hi)
            else:
                if root.val<lo:
                    helper(root.right,lo,hi)
                if root.val>hi:
                    helper(root.left,lo,hi)

        ans=0
        helper(root,low,high)
        return ans