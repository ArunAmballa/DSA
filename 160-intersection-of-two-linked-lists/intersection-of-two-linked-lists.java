/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public int getLength(ListNode head){
        int length=0;
        ListNode temp=head;
        while(temp!=null){
            length+=1;
            temp=temp.next;
        }
        return length;
    }
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lengthA=getLength(headA);
        int lengthB=getLength(headB);
        int count=lengthA-lengthB;
        if(count>0){
            while(count!=0){
                headA=headA.next;
                count=count-1;
            }
        }else{
            while(count!=0){
                headB=headB.next;
                count=count+1;
            }
        }
        while(headA!=null && headB!=null){
            if(headA==headB){
                return headA;
            }
            headA=headA.next;
            headB=headB.next;
        }
        return null;
    }
}