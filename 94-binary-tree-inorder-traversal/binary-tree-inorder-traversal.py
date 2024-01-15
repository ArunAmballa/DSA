# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return None
        inorder=[]
        st=[]
        curr=root
        while curr!=None:
            st.append(curr)
            curr=curr.left
        while st:
            temp=st.pop()
            inorder.append(temp.val)
            node=temp.right
            while node!=None:
                st.append(node)
                node=node.left
        return inorder

        