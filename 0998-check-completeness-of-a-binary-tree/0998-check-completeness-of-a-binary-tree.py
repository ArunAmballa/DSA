# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self,root):
        if root==None:
            return 0
        leftCount=self.countNodes(root.left)
        rightCount=self.countNodes(root.right)
        return leftCount+rightCount+1
    def checkComplete(self,root,n,index):
        if root==None:
            return True
        if index>n:
            return False
        leftCheck=self.checkComplete(root.left,n,2*index)
        rightCheck=self.checkComplete(root.right,n,(2*index)+1)
        return leftCheck and rightCheck
        
         
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        n=self.countNodes(root)
        return self.checkComplete(root,n,1)
        