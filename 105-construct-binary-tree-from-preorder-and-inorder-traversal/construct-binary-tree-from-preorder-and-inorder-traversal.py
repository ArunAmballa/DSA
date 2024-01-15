# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def CBT(self,preorder,inorder,lo,hi,d):
        if lo>hi:
            return None
        ele=preorder[0]
        preorder.pop(0)
        root=TreeNode(ele)
        index=d[ele]
        root.left=self.CBT(preorder,inorder,lo,index-1,d)
        root.right=self.CBT(preorder,inorder,index+1,hi,d)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i
        return self.CBT(preorder,inorder,0,len(preorder)-1,d)
        