# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        st=[]
        st.append(root)
        ans=[]
        while st:
            curr=st.pop()
            ans.append(curr.val)
            if curr.left!=None:
                st.append(curr.left)
            if curr.right!=None:
                st.append(curr.right)
        return ans[::-1]
        