# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,ans):
        if root==None:
            return None
        self.inorder(root.left,ans)
        if root.left==None and root.right==None:
            ans.append(root.val)
        self.inorder(root.right,ans)
        return ans
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        ans=[]
        ans.append(root.val)
        if root.left==None and root.right==None:
            return ans
        if root.left!=None:
            temp=root.left
            while temp!=None and (temp.left!=None or temp.right!=None):
                ans.append(temp.val)
                if temp.left==None:
                    temp=temp.right
                else:
                    temp=temp.left
        ans=self.inorder(root,ans)
        st=[]
        if root.right!=None:
            temp=root.right
            while temp!=None and (temp.left!=None or temp.right!=None):
                st.append(temp.val)
                if temp.right==None:
                    temp=temp.left
                else:
                    temp=temp.right
        
        while st:
            curr=st.pop()
            ans.append(curr)
        return ans
        