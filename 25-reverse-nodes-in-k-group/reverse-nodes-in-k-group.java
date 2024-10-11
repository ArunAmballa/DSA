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
    public int groups=0;
    public int lengthOfLL(ListNode head){
        int length=0;
        ListNode temp=head;
        while(temp!=null){
            length=length+1;
            temp=temp.next;
        }
        return length;
    }
    public ListNode counter(ListNode head,int k){
        int count=1;
        ListNode temp=head;
        while(temp!=null){
            if(count==k){
                break;
            }
            count++;
            temp=temp.next;
        }
        return temp;
    }
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
    public ListNode helper(ListNode head,int times,int k){
        if(head==null|| head.next==null || times>groups){
            return head;
        }
        ListNode reversePoint=counter(head,k);
        ListNode newReversedHead=helper(reversePoint.next,times+1,k);
        reversePoint.next=null;
        ListNode reversedHead=reverse(head);
        head.next=newReversedHead;
        return reversedHead;
    }
    public ListNode reverseKGroup(ListNode head, int k) {
        int length=lengthOfLL(head);
        groups=(length/k);
        return helper(head,1,k);
    }
}