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
        if len(root.children)==0:
            return 1
        n=len(root.children)
        maxHeights=[-1]*n
        print(maxHeights)
        for i in range(len(root.children)):
            maxHeights[i]=self.maxDepth(root.children[i])
        return max(maxHeights)+1
        
        