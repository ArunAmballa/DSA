# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,currSum,targetSum):
        if root==None:
            return False
        currSum=currSum+root.val
        if currSum==targetSum and root.left==None and root.right==None:
            return True
        leftCheck=self.helper(root.left,currSum,targetSum)
        rightCheck=self.helper(root.right,currSum,targetSum)
        return leftCheck or rightCheck
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root,0,targetSum)
        