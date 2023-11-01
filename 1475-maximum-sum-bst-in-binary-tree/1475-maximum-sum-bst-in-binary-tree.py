# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        def helper(root):
            nonlocal maxSum
            if root==None:
                return [True,0,-math.inf,math.inf]
            leftAns=helper(root.left)
            rightAns=helper(root.right)
            if leftAns[0]==True and rightAns[0]==True and root.val>leftAns[2] and root.val<rightAns[3]:
                currSum=leftAns[1]+rightAns[1]+root.val
                maxSum=max(maxSum,currSum)
                return [True,currSum,max(rightAns[2],root.val),min(leftAns[3],root.val)]
            else:
                return [False,max(leftAns[1],rightAns[1]),-math.inf,math.inf]

        maxSum=0
        helper(root)
        return maxSum
        