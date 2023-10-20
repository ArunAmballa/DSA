# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels=[]
        if root==None:
            return levels
        q=Queue()
        q.put([root,0])
        while not q.empty():
            curr,level=q.get()
            if level==len(levels):
                levels.append([])
            levels[level].append(curr.val)
            if curr.left!=None:
                q.put([curr.left,level+1])
            if curr.right!=None:
                q.put([curr.right,level+1])
        return levels
        