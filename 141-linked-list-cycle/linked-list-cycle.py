# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        if head==None or head.next==None:
            return False
        while head!=None:
            if head in s:
                return True
            s.add(head)
            head=head.next
        return False