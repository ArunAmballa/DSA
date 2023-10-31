"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root==None:
            return None
        def helper(root):
            nonlocal prev,head
            if root==None:
                return None
            helper(root.left)
            if prev==None:
                head=root
            else:
                root.left=prev 
                prev.right=root
            prev=root
            helper(root.right)
        prev=None
        head=None
        helper(root)
        prev.right=head
        head.left=prev
        return head
        