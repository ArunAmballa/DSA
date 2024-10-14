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
    public ListNode head;
    public ListNode tail;
    public int capacity;
    public HashMap<Integer,ListNode> map;

    public LRUCache(int capacity) {
        this.capacity=capacity;
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
        remove(node);
        insert(node);
        return node.value; 
    }

    public void remove(ListNode node){
        map.remove(node.key);
        node.prev.next=node.next;
        node.next.prev=node.prev;
    }

    public void insert(ListNode node){
        node.next=head.next;
        node.prev=head;
        node.next.prev=node;
        head.next=node;
        map.put(node.key,node);
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            remove(map.get(key));
        }
        if(map.size()==capacity){
            remove(tail.prev);
        }
        insert(new ListNode(key,value));  
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */