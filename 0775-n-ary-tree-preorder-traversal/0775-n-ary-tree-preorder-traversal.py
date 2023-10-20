"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def order(self,root,ans):
        if root==None:return None
        ans.append(root.val)
        for i in range(len(root.children)):
            self.order(root.children[i],ans)
        return ans
    def preorder(self, root: 'Node') -> List[int]:
        return self.order(root,[])
        