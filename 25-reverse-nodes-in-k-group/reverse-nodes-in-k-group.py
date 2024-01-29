# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head,k,group):
        temp=head
        prev=None
        cnt=0

        while temp!=None and cnt<k:
            forward=temp.next
            temp.next=prev
            prev=temp
            temp=forward
            cnt=cnt+1
        if forward!=None and group!=0:
            head.next=self.reverse(forward,k,group-1)
        else:
            head.next=forward
        return prev
    def length(self,head):
        cnt=0
        temp=head
        while temp!=None:
            cnt=cnt+1
            temp=temp.next
        return cnt
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        size=self.length(head)
        groups=size//k
        return self.reverse(head,k,groups-1)
        