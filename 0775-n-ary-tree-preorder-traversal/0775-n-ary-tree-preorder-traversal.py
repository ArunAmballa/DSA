"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        preOrder=[]
        st=[root]
        while st:
            curr=st.pop()
            preOrder.append(curr.val)
            for i in range(len(curr.children)-1,-1,-1):
                if curr.children[i]!=None:
                    st.append(curr.children[i])
        return preOrder
        