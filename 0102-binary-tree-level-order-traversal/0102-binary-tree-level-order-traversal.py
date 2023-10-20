# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,levels,level):
        if root==None:
            return None
        if len(levels)==level:
            levels.append([])
        levels[level].append(root.val)
        if root.left!=None:
            self.helper(root.left,levels,level+1)
        if root.right!=None:
            self.helper(root.right,levels,level+1)
        return levels
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels=[]
        if root==None:
            return levels
        return self.helper(root,levels,0)
        