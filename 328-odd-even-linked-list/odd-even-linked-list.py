# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead=ListNode(-1)
        evenHead=ListNode(-1)
        oddTail=oddHead
        evenTail=evenHead
        cnt=0
        while head!=None:
            cnt=cnt+1
            if cnt&1==0:
                evenTail.next=head
                evenTail=evenTail.next
            else:
                oddTail.next=head
                oddTail=oddTail.next
            head=head.next
        evenTail.next=None
        oddTail.next=evenHead.next
        return oddHead.next
        