# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        if root.val==p.val or root.val==q.val:
            return root
        leftAns=self.lowestCommonAncestor(root.left,p,q)
        rightAns=self.lowestCommonAncestor(root.right,p,q)

        if leftAns!=None and rightAns!=None:
            return root
        if leftAns==None:
            return rightAns
        if rightAns==None:
            return leftAns
        return root