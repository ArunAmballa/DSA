# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        d=collections.defaultdict(list)
        min_col=0
        max_col=0
        q=Queue()
        q.put([root,0,0])
        while not q.empty():
            node,row,col=q.get()
            min_col=min(min_col,col)
            max_col=max(max_col,col)
            d[col].append((row,node.val))
            if node.left!=None:
                q.put([node.left,row+1,col-1])
            if node.right!=None:
                q.put([node.right,row+1,col+1])
        ans=[]
        for i in range(min_col,max_col+1):
            ans.append([val for row,val in sorted(d[i])])
        return ans

        