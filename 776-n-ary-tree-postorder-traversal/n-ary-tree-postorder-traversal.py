"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        postOrder=[]
        def helper(root):
            nonlocal postOrder
            if root==None:
                return 
            for child in root.children:
                helper(child)
            postOrder.append(root.val)

        helper(root)
        return postOrder
        