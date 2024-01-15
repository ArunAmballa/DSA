# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def continousPath(self,root):
        if root==None:
            return 0
        leftSum=max(self.continousPath(root.left),0)
        rightSum=max(self.continousPath(root.right),0)
        self.ans=max(self.ans,leftSum+rightSum+root.val)
        return max(leftSum,rightSum)+root.val
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=-1<<31
        self.continousPath(root)
        return self.ans
        
        