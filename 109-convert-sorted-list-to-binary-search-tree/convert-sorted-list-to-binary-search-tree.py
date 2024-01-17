# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self,head):
        temp=head
        cnt=0
        while temp!=None:
            cnt=cnt+1
            temp=temp.next
        return cnt
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n=self.countNodes(head)
        def construct(lo,hi):
            nonlocal head
            if lo>hi:
                return None
            mid=(lo+hi)//2
            left=construct(lo,mid-1)
            root=TreeNode(head.val)
            head=head.next
            root.left=left
            right=construct(mid+1,hi)
            root.right=right
            return root
        
        return construct(0,n-1)
        