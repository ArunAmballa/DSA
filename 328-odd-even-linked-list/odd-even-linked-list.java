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
    public ListNode oddEvenList(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode oddList=new ListNode(-1);
        ListNode oddHead=oddList;
        ListNode oddTail=oddList;
        ListNode evenList=new ListNode(-1);
        ListNode evenHead=evenList;
        ListNode evenTail=evenList;
        int cnt=1;
        while(head!=null){
            if(cnt%2==0){
                evenTail.next=head;
                evenTail=evenTail.next;
            }else{
                oddTail.next=head;
                oddTail=oddTail.next;
            }
            head=head.next;
            cnt++;
        }
        evenTail.next=null;
        oddTail.next=evenHead.next;
        return oddHead.next;    
    }
}