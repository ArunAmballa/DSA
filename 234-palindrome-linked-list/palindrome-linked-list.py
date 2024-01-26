# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev=None
        while head!=None:
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        s=head
        f=head.next

        while f!=None and f.next!=None:
            s=s.next
            f=f.next.next
        head1=self.reverse(s.next)

        while head!=None and head1!=None:
            if head1.val!=head.val:
                return False
            head=head.next
            head1=head1.next
        return True

        