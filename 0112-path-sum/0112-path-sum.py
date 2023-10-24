# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,targetSum,currSum):
        if root==None:
            return None
        currSum=currSum+root.val
        if root.left==None and root.right==None and currSum==targetSum:
            return True
        return self.helper(root.left,targetSum,currSum) or self.helper(root.right,targetSum,currSum)

        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root,targetSum,0)