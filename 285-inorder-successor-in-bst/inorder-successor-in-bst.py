# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        ans=0
        curr=root
        while curr!=None:
            if curr.val>p.val:
                ans=curr
                curr=curr.left
            else:
                curr=curr.right
        return ans
        