# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        def helper(nums,lo,hi):
            if lo>hi:
                return None
            mid=(lo+hi)//2
            root=TreeNode(nums[mid])
            root.left=helper(nums,lo,mid-1)
            root.right=helper(nums,mid+1,hi)
            return root
        return helper(nums,0,len(nums)-1)
        