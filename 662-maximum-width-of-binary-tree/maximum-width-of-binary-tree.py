# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        ans=0
        q=Queue()
        q.put([root,1,1])
        while not q.empty():
            n=q.qsize()
            for i in range(n):
                curr,level,index=q.get()
                if i==0:
                    firstIndex=index
                if i==n-1:
                    lastIndex=index
                if curr.left!=None:
                    q.put([curr.left,level+1,2*index])
                if curr.right!=None:
                    q.put([curr.right,level+1,2*index+1])
            ans=max(ans,lastIndex-firstIndex+1)
        return ans


        