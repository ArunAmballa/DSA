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
    public int lengthOfLL(ListNode head){
        int length=0;
        ListNode temp=head;
        while(temp!=null){
            length=length+1;
            temp=temp.next;
        }
        return length;
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
    public ListNode helper(ListNode head,int t){
        int count=1;
        ListNode temp=head;
        while(temp!=null){
            if(count==t){
                break;
            }
            count++;
            temp=temp.next;
        }
        return temp;
    }
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null || head.next==null){
            return head;
        }
        int total=lengthOfLL(head);
        if(k>total) k=k%total;
        int point=total-k;
        if(point==0) return head;
        ListNode reversePoint =helper(head,point);
        ListNode newReversedHead=reverse(reversePoint.next);
        reversePoint.next=null;
        ListNode reversedHead=reverse(head);
        head.next=newReversedHead;
        return reverse(reversedHead);
    }
}