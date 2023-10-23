# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder=[]
        curr=root
        while curr!=None:
            if curr.right==None:
                preorder.append(curr.val)
                curr=curr.left
            else:
                pred=curr.right
                while pred.left!=None and pred.left!=curr:
                    pred=pred.left
                if pred.left==None:
                    pred.left=curr
                    preorder.append(curr.val)
                    curr=curr.right
                else:
                    pred.left=None
                    curr=curr.left
        preorder.reverse()
        return preorder
        