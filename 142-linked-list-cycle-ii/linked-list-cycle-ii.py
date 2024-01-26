# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        s=head
        f=head
        e=head
        while f!=None and f.next!=None:
            s=s.next
            f=f.next.next
            if s==f:
                while s!=e:
                    s=s.next
                    e=e.next
                return e
        return None
        