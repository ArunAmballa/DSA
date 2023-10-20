# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:return []
        q=Queue()
        q.put(root)
        q.put(None)
        ans=[]
        l=[]
        while q.empty()==False:
            curr=q.get()
            if curr==None:
                if q.empty()==True:
                    ans.append(l.copy())
                    l.clear()
                    break
                else:
                    q.put(None)
                ans.append(l.copy())
                l.clear()
            else:
                l.append(curr.val)
                if curr.left!=None:
                    q.put(curr.left)
                if curr.right!=None:
                    q.put(curr.right)
        return ans 