# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.val
        def helper(root):
            nonlocal maxPath
            if root==None:
                return -(1<<31)
            leftCont=max(helper(root.left),0)
            rightCont=max(helper(root.right),0)
            maxPath=max(maxPath,leftCont+rightCont+root.val)
            return max(leftCont,rightCont)+root.val
        
        maxPath=-(1<<31)
        helper(root)
        return maxPath

        