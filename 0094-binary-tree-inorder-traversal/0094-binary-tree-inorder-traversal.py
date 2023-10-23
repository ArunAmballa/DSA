# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder=[]
        curr=root
        while curr!=None:
            if curr.left==None:
                inorder.append(curr.val)
                curr=curr.right
            else:
                pred=curr.left
                while pred.right!=None and pred.right!=curr:
                    pred=pred.right
                if pred.right==None:
                    pred.right=curr
                    curr=curr.left
                else:
                    pred.right=None
                    inorder.append(curr.val)
                    curr=curr.right
        return inorder
        