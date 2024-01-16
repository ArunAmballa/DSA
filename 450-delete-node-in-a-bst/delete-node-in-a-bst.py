# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMax(self,root):
        temp=root
        while temp.right!=None:
            temp=temp.right
        return temp.val
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root==None:
            return None
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
            return root
        if key>root.val:
            root.right=self.deleteNode(root.right,key)
            return root
        if root.left==None and root.right==None:
            return None
        if root.left==None:
            return root.right
        if root.right==None:
            return root.left
        root.val=self.getMax(root.left)
        root.left=self.deleteNode(root.left,root.val)
        return root