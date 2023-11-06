# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None or (root.left==None and root.right==None):
            return True
        def helper(root):
            if root==None:
                return 0
            leftHeight=helper(root.left)
            if leftHeight==-1:
                return -1
            rightHeight=helper(root.right)
            if rightHeight==-1:
                return -1
            if abs(leftHeight-rightHeight)>1:
                return -1
            return max(leftHeight,rightHeight)+1
        height=helper(root)
        if height==-1:
            return False
        return True
        