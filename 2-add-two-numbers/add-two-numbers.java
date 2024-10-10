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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head=new ListNode(-1);
        ListNode temp=head;
        int carry=0;
        while(l1!=null || l2!=null || carry!=0){
            int sum=0;
            if(l1!=null) sum=sum+l1.val;
            if(l2!=null) sum=sum+l2.val;
            sum=sum+carry;
            int element=sum%10;
            ListNode newNode=new ListNode(element);
            newNode.next=null;
            temp.next=newNode;
            temp=temp.next;
            carry=sum/10;
            if(l1!=null) l1=l1.next;
            if(l2!=null) l2=l2.next;
        }
        return head.next;
        
    }
}