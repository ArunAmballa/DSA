/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head==null || head.next==null){
            return null;
        }
        ListNode fast=head;
        ListNode slow=head;
        ListNode e=head;
        while(fast!=null && fast.next!=null){
            fast=fast.next.next;
            slow=slow.next;
            if(slow==fast){
                while(e!=slow){
                    e=e.next;
                    slow=slow.next;
                }
                return e;
            }
        }
        return null;
        
    }
}