# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def CBT(self,inorderArray,lo,hi):
        if lo>hi:
            return 
        mid=(lo+hi)//2
        ele=inorderArray[mid]
        root=TreeNode(ele)
        root.left=self.CBT(inorderArray,lo,mid-1)
        root.right=self.CBT(inorderArray,mid+1,hi)
        return root
    def inorder(self,root):
        if root==None:
            return None
        self.inorder(root.left)
        self.inorderArray.append(root.val)
        self.inorder(root.right)
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorderArray=[]
        self.inorder(root)
        return self.CBT(self.inorderArray,0,len(self.inorderArray)-1)
        