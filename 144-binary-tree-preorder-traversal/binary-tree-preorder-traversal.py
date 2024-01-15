# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder=[]
        if root==None:
            return []
        curr=root
        while curr!=None:
            if curr.left==None:
                preorder.append(curr.val)
                curr=curr.right
            else:
                pred=curr.left
                while pred.right!=None and pred.right!=curr:
                    pred=pred.right
                if pred.right==None:
                    pred.right=curr
                    preorder.append(curr.val)
                    curr=curr.left
                else:
                    # pred.right=None
                    curr=curr.right
        return preorder
        