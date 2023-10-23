# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root):
        if root==None:
            return None
        if root.left==None and root.right==None:
            self.boundary.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    def leftboundary(self,root):
        curr=root
        while curr!=None:
            if curr.left!=None or curr.right!=None:
                self.boundary.append(curr.val)
            if curr.left==None:
                curr=curr.right
            else:
                curr=curr.left
    def rightboundary(self,root):
        curr=root
        temp=[]
        while curr!=None:
            if curr.left!=None or curr.right!=None:
                temp.append(curr.val)
            if curr.right==None:
                curr=curr.left
            else:
                curr=curr.right
        for i in range(len(temp)-1,-1,-1):
            self.boundary.append(temp[i])
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.boundary=[]
        if root==None:
            return self.boundary
        if root.left==None and root.right==None:
            self.boundary.append(root.val)
            return self.boundary
        else:
            self.boundary.append(root.val)
        self.leftboundary(root.left)
        self.preorder(root)
        self.rightboundary(root.right)
        return self.boundary

        