# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        temp=dummy
        if head==None:
            return None
        st=[]
        while head!=None:
            st.append(head)
            head=head.next
        while st:
            curr=st.pop()
            temp.next=curr
            temp=temp.next
        temp.next=None
        return dummy.next