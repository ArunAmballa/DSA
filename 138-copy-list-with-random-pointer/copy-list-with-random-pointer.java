/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head==null){
            return head;
        }
        HashMap<Node,Node> map=new HashMap<>();
        Node temp1=head;
        Node dummy=new Node(-1);
        Node temp2=dummy;
        while(temp1!=null){
            Node newNode=new Node(temp1.val);
            map.put(temp1,newNode);
            temp2.next=newNode;
            temp2=temp2.next;
            temp1=temp1.next;
        }
        Node temp3=head;
        Node temp4=dummy.next;
        while(temp3!=null){
            temp4.random=map.getOrDefault(temp3.random,null);
            temp3=temp3.next;
            temp4=temp4.next;
        }
        return dummy.next;
    }
}