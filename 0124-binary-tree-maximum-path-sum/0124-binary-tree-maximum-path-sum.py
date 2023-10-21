# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if root==None:
            return 0
        lsum=max(self.helper(root.left),0)
        rsum=max(self.helper(root.right),0)
        self.maxi=max(self.maxi,(root.val+lsum+rsum))
        print(self.maxi)
        return max(lsum,rsum)+root.val
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=-(1<<31)
        self.helper(root)
        return self.maxi
        