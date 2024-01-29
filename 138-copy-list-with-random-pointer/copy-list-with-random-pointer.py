"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return head
        d={}
        head1=Node(head.val)
        temp1=head1
        temp=head.next
        d[head]=head1
        while temp!=None:
            temp1.next=Node(temp.val)
            temp1=temp1.next
            d[temp]=temp1
            temp=temp.next
        p1=head
        p2=head1
        while p1!=None:
            p2.random=d.get(p1.random,None)
            p2=p2.next
            p1=p1.next
        return head1
        