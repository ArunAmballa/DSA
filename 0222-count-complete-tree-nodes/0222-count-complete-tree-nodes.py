# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findleft(self,root):
        ht=0
        while root!=None:
            ht=ht+1
            root=root.left
        return ht
    def findright(self,root):
        ht=0
        while root!=None:
            ht=ht+1
            root=root.right
        return ht
    def count(self,root):
        if root==None:return 0
        lh=self.findleft(root.left)
        rh=self.findright(root.right)
        if lh==rh:
            return (1<<lh+1)-1
        return self.count(root.left)+self.count(root.right)+1
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.count(root)
        