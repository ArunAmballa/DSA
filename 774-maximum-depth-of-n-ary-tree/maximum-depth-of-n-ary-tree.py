"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        ans=[]
        for child in root.children:
            height=self.maxDepth(child)
            ans.append(height)
        return max(ans)+1 if len(ans)>0 else 1