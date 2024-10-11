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
    public ListNode deleteDuplicatesUnsorted(ListNode head) {

        HashMap<Integer,Integer> map=new HashMap<>();
        ListNode temp=head;
        while(temp!=null){
            map.put(temp.val,map.getOrDefault(temp.val,0)+1);
            temp=temp.next;
        }
        System.out.println(map.toString());
        ListNode newHead=new ListNode(-1);
        newHead.next=head;
        ListNode temp1=newHead;
        while(temp1!=null){
            if(temp1.next!=null && map.get(temp1.next.val)>1){
                temp1.next=temp1.next.next;
            }else{
                temp1=temp1.next;
            }
        }
        return newHead.next; 
    }
}