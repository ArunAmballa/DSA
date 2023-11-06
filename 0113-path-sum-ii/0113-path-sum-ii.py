# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root==None:
            return []
        def helper(root,l,currSum,targetSum):
            nonlocal ans
            if root==None:
                return None
            currSum=currSum+root.val
            l=l+[root.val]
            if currSum==targetSum and root.left==None and root.right==None:
                ans.append(l)
                return 
            helper(root.left,l,currSum,targetSum)
            helper(root.right,l,currSum,targetSum)

        ans=[]
        helper(root,[],0,targetSum)
        return ans
        