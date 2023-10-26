# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Solution:
    def parentMapping(self,root,parentMap):
        q=Queue()
        q.put(root)
        while not q.empty():
            curr=q.get()
            if curr.left!=None:
                parentMap[curr.left]=curr
                q.put(curr.left)
            if curr.right!=None:
                parentMap[curr.right]=curr
                q.put(curr.right)
    def findNodes(self,targetNode,parentMap,k):
        q=Queue()
        q.put([targetNode,0])
        visited={targetNode:1}
        ans=[]
        while not q.empty():
            curr,distance=q.get()
            if distance==k:
                ans.append(curr.val)
            if curr.left!=None and visited.get(curr.left,0)!=1:
                q.put([curr.left,distance+1])
                visited[curr.left]=1
            if curr.right!=None and visited.get(curr.right,0)!=1:
                q.put([curr.right,distance+1])
                visited[curr.right]=1
            if parentMap[curr]!=None and visited.get(parentMap[curr],0)!=1:
                q.put([parentMap[curr],distance+1])
                visited[parentMap[curr]]=1
        return ans



    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root==None or target==None:
            return []
        parentMap={root:None}
        self.parentMapping(root,parentMap)
        return self.findNodes(target,parentMap,k)
        