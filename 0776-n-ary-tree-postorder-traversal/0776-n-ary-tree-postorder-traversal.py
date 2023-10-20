"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def order(self,root,ans):
        if root==None:
            return None
        for i in range(len(root.children)):
            self.order(root.children[i],ans)
        ans.append(root.val)
        return ans
    def postorder(self, root: 'Node') -> List[int]:
        return self.order(root,[])
        
        
        