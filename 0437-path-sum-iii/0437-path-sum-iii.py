# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,preSum,d,targetSum):
        if root==None:
            return None
        preSum=preSum+root.val
        checkSum=preSum-targetSum
        if checkSum in d:
            self.ans=self.ans+d[checkSum]
        d[preSum]=d.get(preSum,0)+1
        self.helper(root.left,preSum,d,targetSum)
        self.helper(root.right,preSum,d,targetSum)
        d[preSum]=d[preSum]-1
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d={0:1}
        self.ans=0
        self.helper(root,0,d,targetSum)
        return self.ans