# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if root==None:
            #isBST,Size,MaxValue,MinValue
            return [True,0,-math.inf,math.inf]
        leftCheck=self.helper(root.left)
        rightCheck=self.helper(root.right)
        if ((leftCheck[0]==True) and (rightCheck[0]==True) and (root.val>leftCheck[2]) and (root.val<rightCheck[3])):
            currSize=leftCheck[1]+rightCheck[1]+root.val
            self.maxSum=max(self.maxSum,currSize)
            return [True,currSize,max(root.val,rightCheck[2]),min(root.val,leftCheck[3])]
        return [False,max(leftCheck[1],rightCheck[1]),-math.inf,math.inf]
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        self.maxSum=0
        self.helper(root)
        return self.maxSum
        