# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,d,k):
        if root==None:
            return None
        target=k-root.val
        if target in d:
            return True
        d[root.val]=1
        leftAns=self.helper(root.left,d,k)
        rightAns=self.helper(root.right,d,k)
        return leftAns or rightAns
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        d={}
        return self.helper(root,d,k)
        