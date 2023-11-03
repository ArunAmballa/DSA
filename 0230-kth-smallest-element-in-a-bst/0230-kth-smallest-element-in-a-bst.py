# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return -1
        def helper(root):
            nonlocal k,maxValue
            if root==None:
                return -1
            helper(root.left)
            k=k-1
            if k==0:
                maxValue=root.val
            helper(root.right)
        maxValue=0
        helper(root)
        return maxValue
