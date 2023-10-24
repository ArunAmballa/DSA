# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,targetSum,currSum,l,ans):
        if root==None:
            return None
        currSum=currSum+root.val
        l=l+[root.val]
        if root.left==None and root.right==None and currSum==targetSum:
            ans.append(l.copy())
            return ans
        self.helper(root.left,targetSum,currSum,l,ans)
        self.helper(root.right,targetSum,currSum,l,ans)
        return ans
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.helper(root,targetSum,0,[],[])