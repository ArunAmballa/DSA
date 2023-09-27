# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:return None
        h=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h,(lists[i].val,i))
        dummy=ListNode(-1)
        temp=dummy
        while h:
            val,index=heapq.heappop(h)
            temp.next=lists[index]
            temp=temp.next
            if lists[index].next!=None:
                heapq.heappush(h,(lists[index].next.val,index))
                lists[index]=lists[index].next
        return dummy.next
        