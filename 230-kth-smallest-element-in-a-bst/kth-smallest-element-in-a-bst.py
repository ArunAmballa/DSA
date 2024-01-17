# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return 0
        def helper(root,k):
            nonlocal cnt,ans
            if root==None:
                return None
            helper(root.left,k)
            cnt=cnt+1
            if cnt==k:
                ans=root.val
            helper(root.right,k)
        
        cnt=0
        ans=0
        helper(root,k)
        return ans

        