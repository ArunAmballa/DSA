# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddListHead=ListNode(-1)
        oddListTail=oddListHead
        evenListHead=ListNode(-1)
        evenListTail=evenListHead
        cnt=0
        while head!=None:
            cnt=cnt+1
            if cnt%2==0:
                evenListTail.next=head
                head=head.next
                evenListTail=evenListTail.next
            else:
                oddListTail.next=head
                head=head.next
                oddListTail=oddListTail.next
        evenListTail.next=None
        oddListTail.next=evenListHead.next
        return oddListHead.next
        