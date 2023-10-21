# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        min_level=0
        max_level=0
        q=Queue()
        d={}
        q.put([root,0])
        while not q.empty():
            curr,level=q.get()
            min_level=min(min_level,level)
            max_level=max(max_level,level)
            if level not in d:
                d[level]=[]
            d[level].append(curr.val)
            if curr.left!=None:
                q.put([curr.left,level-1])
            if curr.right!=None:
                q.put([curr.right,level+1])
        ans=[]
        for i in range(min_level,max_level+1):
            ans.append(d[i])
        return ans