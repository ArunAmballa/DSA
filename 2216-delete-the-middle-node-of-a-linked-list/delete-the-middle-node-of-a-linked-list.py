# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None
        d=ListNode(-1)
        temp=d
        temp.next=head
        s=d
        f=d.next
        while f!=None and f.next!=None:
            s=s.next
            f=f.next.next
        s.next=s.next.next
        return head
        