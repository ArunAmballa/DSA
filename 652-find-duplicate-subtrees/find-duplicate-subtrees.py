# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if root==None:
            return "N"
        leftEncode=self.helper(root.left)
        rightEncode=self.helper(root.right)
        currEncode=str(root.val)+","+leftEncode+","+rightEncode
        if currEncode not in self.d:
            self.d[currEncode]=1
        else:
            if self.d[currEncode]==1:
                self.ans.append(root)
            self.d[currEncode]=self.d.get(currEncode,0)+1
        return currEncode
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if root==None:
            return None
        self.ans=[]
        self.d={}
        self.helper(root)
        return self.ans
        