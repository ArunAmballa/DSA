"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        st=[root]
        postOrder=[]
        while st:
            curr=st.pop()
            postOrder.append(curr.val)
            for i in range(len(curr.children)):
                if curr.children[i]!=None:
                    st.append(curr.children[i])
        return postOrder[::-1]
        