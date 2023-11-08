# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if root==None:
            return None
        self.inorder(root.left)
        self.order.append(root.val)
        self.inorder(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.order=[]
        self.inorder(root)
        self.order.sort()
        print(self.order)
        def helper(root):
            nonlocal index
            if index>=len(self.order) or root==None:
                return 
            helper(root.left)
            root.val=self.order[index]
            index=index+1
            helper(root.right)
            return root
        n=len(self.order)
        index=0
        return helper(root)
        