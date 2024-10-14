/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverse(ListNode head){
        ListNode prev=null;
        ListNode temp=null;
        while(head!=null){
            temp=head.next;
            head.next=prev;
            prev=head;
            head=temp;
        }
        return prev;
    }
    public int pairSum(ListNode head) {
        if(head==null || head.next==null){
            return 0;
        }
        ListNode slow=head;
        ListNode fast=head.next;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        ListNode head2=reverse(slow.next);
        slow.next=null;
        int maxi=-1;
        while(head!=null && head2!=null){
            maxi=Math.max(maxi,head.val+head2.val);
            head=head.next;
            head2=head2.next;
        }
        return maxi; 
    }
}