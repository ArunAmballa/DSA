# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bst(self,pre,ub):
        if self.i==len(pre) or pre[self.i]>ub:
            return None
        root=TreeNode(pre[self.i])
        self.i=self.i+1
        root.left=self.bst(pre,root.val)
        root.right=self.bst(pre,ub)
        return root
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i=0
        return self.bst(preorder,math.inf)
        