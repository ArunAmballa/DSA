# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructBinaryTree(self,inorder,postorder,lo,hi,d):
        if lo>hi:
            return 
        ele=postorder.pop()
        root=TreeNode(ele)
        index=d[ele]
        root.right=self.constructBinaryTree(inorder,postorder,index+1,hi,d)
        root.left=self.constructBinaryTree(inorder,postorder,lo,index-1,d)
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i
        return self.constructBinaryTree(inorder,postorder,0,len(postorder)-1,d)