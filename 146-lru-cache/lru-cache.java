class ListNode{
    public int key;
    public int value;
    public ListNode next;
    public ListNode prev;
    public ListNode(int key,int value){
        this.key=key;
        this.value=value;
        this.next=null;
        this.prev=null;
    }
}
class LRUCache {

    public int currentCapacity;
    public ListNode head;
    public ListNode tail;
    public int capacity;
    public HashMap<Integer,ListNode> map;

    public LRUCache(int capacity) {
        this.capacity=capacity;
        this.currentCapacity=0;
        this.head=new ListNode(-1,-1);
        this.tail=new ListNode(-1,-1);
        head.next=tail;
        tail.prev=head;
        this.map=new HashMap<>();
    }
    
    public int get(int key) {
        if(!map.containsKey(key)){
            return -1;
        }
        ListNode node=map.get(key);
        node.prev.next=node.next;
        node.next.prev=node.prev;
        node.next=head.next;
        node.prev=head;
        node.next.prev=node;
        head.next=node;
        return node.value; 
    }
    
    public void put(int key, int value) {
        if(currentCapacity<capacity){
            if(!map.containsKey(key)){
                ListNode newNode=new ListNode(key,value);
                newNode.next=head.next;
                newNode.prev=head;
                newNode.next.prev=newNode;
                head.next=newNode;
                map.put(key,newNode);
                currentCapacity=currentCapacity+1;
            }else{
                ListNode node=map.get(key);
                node.prev.next=node.next;
                node.next.prev=node.prev;
                node.next=head.next;
                node.prev=head;
                node.next.prev=node;
                head.next=node;
                node.value=value;
            }  
        }else{
            if(map.containsKey(key)){
                ListNode node=map.get(key);
                node.prev.next=node.next;
                node.next.prev=node.prev;
                node.next=head.next;
                node.prev=head;
                node.next.prev=node;
                head.next=node;
                node.value=value;
            }else{
                ListNode removedNode=tail.prev;
                removedNode.prev.next=removedNode.next;
                removedNode.next.prev=removedNode.prev;
                map.remove(removedNode.key);
                currentCapacity=currentCapacity-1;
                ListNode newNode=new ListNode(key,value);
                newNode.next=head.next;
                newNode.prev=head;
                newNode.next.prev=newNode;
                head.next=newNode;
                map.put(key,newNode);
                currentCapacity=currentCapacity+1;
            }
            
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */