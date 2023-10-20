# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,ans,st):
        if root==None:
            return ans
        st.append(root)
        while st:
            curr=st.pop()
            ans.append(curr.val)
            if curr.right!=None:
                st.append(curr.right)
            if curr.left!=None:
                st.append(curr.left)
        return ans
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preorder(root,[],[])
        
        