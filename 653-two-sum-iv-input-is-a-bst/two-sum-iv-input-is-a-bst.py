# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,k):
        if root==None:
            return None
        target=k-root.val
        if target in self.d:
            self.ans=True
        self.d[root.val]=1
        self.helper(root.left,k)
        self.helper(root.right,k)
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.d={}
        self.ans=False
        self.helper(root,k)
        return self.ans
        