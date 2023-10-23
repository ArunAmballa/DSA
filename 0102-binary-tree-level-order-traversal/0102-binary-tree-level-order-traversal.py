# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,level,levels):
        if root==None:
            return None
        if len(levels)==level:
            levels.append([])
        levels[level].append(root.val)
        self.helper(root.left,level+1,levels)
        self.helper(root.right,level+1,levels)
        return levels
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        return self.helper(root,0,[])