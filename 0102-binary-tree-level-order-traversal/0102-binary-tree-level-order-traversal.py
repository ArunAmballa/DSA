# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d={}
        if root==None:
            return []
        q=collections.deque([(root,0)])
        while q:
            curr,level=q.popleft()
            if level not in d:
                d[level]=[]
            d[level].append(curr.val)
            if curr.left!=None:
                q.append([curr.left,level+1])
            if curr.right!=None:
                q.append([curr.right,level+1])
        return d.values()
        
        