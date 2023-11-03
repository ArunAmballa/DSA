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
    def findSize(self,head):
        temp=head
        c=0
        while temp!=None:
            c=c+1
            temp=temp.next
        return c
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n=self.findSize(head)
        def helper(n):
            nonlocal head
            if n<=0 or head==None:
                return None
            leftAns=helper(n-1-n//2)
            root=TreeNode(head.val)
            root.left=leftAns
            head=head.next
            root.right=helper(n//2)
            return root
        return helper(n)
        