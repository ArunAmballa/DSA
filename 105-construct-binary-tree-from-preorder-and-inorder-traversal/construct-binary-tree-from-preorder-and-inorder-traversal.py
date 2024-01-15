# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i
        def CBT(inorder,preorder,lo,hi):
            nonlocal index
            if lo>hi or index>len(preorder)-1:
                return None
            ele=preorder[index]
            index=index+1
            root=TreeNode(ele)
            ind=d[ele]
            root.left=CBT(inorder, preorder, lo, ind-1)
            root.right=CBT(inorder, preorder, ind+1, hi)
            return root
        index=0
        return CBT(inorder,preorder,0,len(preorder))
        