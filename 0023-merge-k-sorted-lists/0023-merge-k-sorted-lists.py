# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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
    def helper(self,lists,last):
        while last!=0:
            i=0
            j=last
            while i<j:
                lists[i]=self.merge(lists[i],lists[j])
                i=i+1
                j=j-1
                if i>=j:
                    last=j
        return lists[0]
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:return None
        return self.helper(lists,len(lists)-1)
        