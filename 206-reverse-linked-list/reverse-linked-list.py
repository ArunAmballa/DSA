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
            st.append(head.val)
            head=head.next
        while st:
            curr=st.pop()
            temp.next=ListNode(curr)
            temp=temp.next
        return dummy.next