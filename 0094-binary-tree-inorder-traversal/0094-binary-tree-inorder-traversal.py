# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        ans=[]
        st=[]
        while root!=None:
            st.append(root)
            root=root.left
        while st:
            curr=st.pop()
            ans.append(curr.val)
            curr=curr.right
            while curr!=None:
                st.append(curr)
                curr=curr.left
        return ans        