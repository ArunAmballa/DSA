# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,currSum,l,ans,targetSum):
        if root==None:
            return []
        currSum=currSum+root.val
        l=l+[root.val]
        if currSum==targetSum and (root.left==None and root.right==None):
            ans.append(l)
        self.helper(root.left, currSum, l, ans, targetSum)
        self.helper(root.right, currSum, l, ans, targetSum)
        return ans
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.helper(root,0,[],[],targetSum)