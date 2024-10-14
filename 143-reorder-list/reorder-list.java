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
    public void reorderList(ListNode head) {
        ListNode slow=head;
        ListNode fast=head.next;
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }
        ListNode head2=reverse(slow.next);
        slow.next=null;
        ListNode newHead=new ListNode(-1);
        ListNode temp=newHead;
        ListNode temp1=head;
        int cnt=0;
        while(temp1!=null && head2!=null){
            if(cnt%2==0){
                temp.next=temp1;
                temp=temp.next;
                temp1=temp1.next;
            }else{
                temp.next=head2;
                temp=temp.next;
                head2=head2.next;
            }
            cnt++;
        }
        if(temp1!=null){
            temp.next=temp1;
            temp=temp.next;
            temp1=temp1.next;
        }
        if(head2!=null){
            temp.next=head2;
            head2=head2.next;
            temp=temp.next;
        }
    }
}