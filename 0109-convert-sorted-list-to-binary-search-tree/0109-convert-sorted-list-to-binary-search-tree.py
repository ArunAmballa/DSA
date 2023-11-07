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
        cnt=0
        while temp!=None:
            cnt=cnt+1
            temp=temp.next
        return cnt
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n=self.findSize(head)
        def helper(n):
            nonlocal head
            if n<=0:
                return None
            leftAns=helper(n-1-n//2)
            root=TreeNode(head.val)
            head=head.next
            root.left=leftAns
            rightAns=helper(n//2)
            root.right=rightAns
            return root
        return helper(n)

        