# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        def helper(root):
            nonlocal ans
            if root==None:
                return True
            leftHeight=helper(root.left)
            rightHieght=helper(root.right)
            if abs(leftHeight-rightHieght)>1:
                ans=False
            return max(leftHeight,rightHieght)+1
        ans=True
        helper(root)
        return ans

        