"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def helper(self,root,preOrder):
        if root==None:
            return None
        preOrder.append(root.val)
        for i in range(len(root.children)):
            self.helper(root.children[i],preOrder)
        return preOrder
    def preorder(self, root: 'Node') -> List[int]:
        return self.helper(root,[])