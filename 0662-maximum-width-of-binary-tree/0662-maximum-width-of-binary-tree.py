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
        max_width=0
        q=Queue()
        q.put([root,1,1])
        prevLevel=0
        first=0
        while not q.empty():
            curr,index,level=q.get()
            if level>prevLevel:
                first=index
                prevLevel=level
            max_width=max(max_width,index-first+1)
            if curr.left!=None:
                q.put([curr.left,2*index,level+1])
            if curr.right!=None:
                q.put([curr.right,(2*index)+1,level+1])
        return max_width
            

        