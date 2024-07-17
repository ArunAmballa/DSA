# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if root==None:
            return ans
        q=deque()
        q.append([root,0])
        while q:
            node,level=q.popleft()
            if len(ans)==level:
                ans.append([])
            ans[level].append(node.val)
            if node.left!=None:
                q.append([node.left,level+1])
            if node.right!=None:
                q.append([node.right,level+1])
        return ans

        