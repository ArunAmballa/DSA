# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        def helper(root,curr):
            nonlocal ans
            if root==None:
                return 0
            curr=curr*10+root.val
            if root.left==None and root.right==None:
                ans=ans+curr
            helper(root.left,curr)
            helper(root.right,curr)
        

        ans=0
        helper(root,0)
        return ans
        