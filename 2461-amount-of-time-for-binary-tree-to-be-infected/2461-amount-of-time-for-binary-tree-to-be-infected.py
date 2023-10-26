# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def parentMapping(self,root,target,parentMap):
        targetNode=None
        q=Queue()
        q.put(root)
        while not q.empty():
            curr=q.get()
            if curr.val==target:
                targetNode=curr
            if curr.left!=None:
                q.put(curr.left)
                parentMap[curr.left]=curr
            if curr.right!=None:
                q.put(curr.right)
                parentMap[curr.right]=curr
        return targetNode
        
                
    def burningTime(self,targetNode,parentMap):
        time=0
        m=Queue()
        m.put(targetNode)
        isBurnt={targetNode:1}
        while not m.empty():
            size=m.qsize()
            fireSpreaded=False
            for i in range(0,size):
                curr=m.get()
                if curr.left!=None and isBurnt.get(curr.left,0)!=1:
                    m.put(curr.left)
                    isBurnt[curr.left]=1
                    fireSpreaded=True
                if curr.right!=None and isBurnt.get(curr.right,0)!=1:
                    m.put(curr.right)
                    isBurnt[curr.right]=1
                    fireSpreaded=1
                if parentMap[curr]!=None and isBurnt.get(parentMap[curr],0)!=1:
                    m.put(parentMap[curr])
                    isBurnt[parentMap[curr]]=1
                    fireSpreaded=True
            if fireSpreaded==True:
                time=time+1
        return time
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if root==None:
            return 0
        parentMap={root:None}
        targetNode=self.parentMapping(root,start,parentMap)
        if targetNode==None:
            return 0
        return self.burningTime(targetNode,parentMap)