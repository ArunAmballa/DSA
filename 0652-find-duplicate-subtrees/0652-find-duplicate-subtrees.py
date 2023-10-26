# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,d):
        if root==None:
            return "N"
        leftEncode=self.helper(root.left,d)
        rightEncode=self.helper(root.right,d)
        currEncode=str(root.val)+ "," + leftEncode + "," + rightEncode
        if currEncode in d:
            if d[currEncode]==1:
                self.ans.append(root)
            d[currEncode]=d.get(currEncode,0)+1
        else:
            d[currEncode]=1
        return currEncode

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.ans=[]
        if root==None:
            return self.ans
        self.helper(root,{})
        return self.ans
        