"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from queue import Queue
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels=[]
        if root==None:
            return levels
        q=Queue()
        q.put([root,0])
        while not q.empty():
            curr,level=q.get()
            if len(levels)==level:
                levels.append([])
            levels[level].append(curr.val)
            for i in range(len(curr.children)):
                if curr.children[i]!=None:
                    q.put([curr.children[i],level+1])
        return levels
        