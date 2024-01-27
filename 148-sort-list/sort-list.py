# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self,head):
        s=head
        f=head
        while f.next!=None and f.next.next!=None:
            s=s.next
            f=f.next.next
        return s
    def merge(self,head1,head2):
        dummy=ListNode(-1)
        temp=dummy
        while head1!=None and head2!=None:
            if head1.val<=head2.val:
                temp.next=head1
                head1=head1.next
            else:
                temp.next=head2
                head2=head2.next
            temp=temp.next
        if head1!=None:
            temp.next=head1
        if head2!=None:
            temp.next=head2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        mid=self.findMid(head)
        right=mid.next
        mid.next=None
        return self.merge(self.sortList(head),self.sortList(right))

        