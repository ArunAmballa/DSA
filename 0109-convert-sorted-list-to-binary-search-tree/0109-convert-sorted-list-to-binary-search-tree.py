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
        c=0
        temp=head
        while temp!=None:
            c=c+1
            temp=temp.next
        return c
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        size=self.findSize(head)
        print(size)
        def helper(n):
            nonlocal head
            if n<=0 or head==None:
                return None
            leftTree=helper(n-1-n//2)
            root=TreeNode(head.val)
            root.left=leftTree
            head=head.next
            root.right=helper(n//2)
            return root
        return helper(size)
        