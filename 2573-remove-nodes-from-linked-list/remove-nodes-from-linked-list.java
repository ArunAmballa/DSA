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
        if(head==null || head.next==null){
            return head;
        }
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
    public ListNode removeNodes(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode newHead=reverse(head);
        ListNode temp=newHead;
        int maxi=temp.val;
        while(temp!=null){
            if(temp.next!=null && temp.next.val<temp.val){
                temp.next=temp.next.next;
            }else{
                if(temp.next!=null) maxi=Math.max(maxi,temp.next.val);
                temp=temp.next;
            }
        }
        return reverse(newHead);  
    }
}