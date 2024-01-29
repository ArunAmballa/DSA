# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head,k,groups):
        if head==None or head.next==None:
            return head
        prev=None
        temp=head
        cnt=0
        while temp!=None and cnt<k:
            forward=temp.next
            temp.next=prev
            prev=temp
            temp=forward
            cnt=cnt+1
        if forward!=None and groups!=0:
            head.next=self.reverse(forward,k,groups-1)
        else:
            head.next=forward
        return prev
    def size(self,head):
        cnt=0
        temp=head
        while temp!=None:
            cnt+=1
            temp=temp.next
        return cnt
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        length=self.size(head)
        number=length//k
        return self.reverse(head,k,number-1)
