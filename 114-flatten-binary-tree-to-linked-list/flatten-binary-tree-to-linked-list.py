# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None:
            return None
        st=[]
        st.append(root)
        while st:
            curr=st.pop()
            if curr.right!=None:
                st.append(curr.right)
            if curr.left!=None:
                st.append(curr.left)
            if st:
                curr.right=st[-1]
            curr.left=None
    