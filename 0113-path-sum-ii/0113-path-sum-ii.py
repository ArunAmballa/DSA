# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,l,ans,currSum,targetSum):
        if root==None:
            return None
        l=l+[root.val]
        currSum=currSum+root.val
        if root.left==None and root.right==None and currSum==targetSum:
            ans.append(l)
            return ans
        self.helper(root.left,l,ans,currSum,targetSum)
        self.helper(root.right,l,ans,currSum,targetSum)
        return ans

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.helper(root,[],[],0,targetSum)
        