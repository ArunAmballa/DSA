# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels=[]
        if root==None:
            return levels
        q=Queue()
        q.put([root,0])
        while not q.empty():
            n=q.qsize()
            l=[-1]*n
            for i in range(n):
                curr,level=q.get()
                index=i if level%2==0 else  n-i-1
                l[index]=curr.val
                if curr.left!=None:
                    q.put([curr.left,level+1])
                if curr.right!=None:
                    q.put([curr.right,level+1])
            levels.append(l)
        return levels
        