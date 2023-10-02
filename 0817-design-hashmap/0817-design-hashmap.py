class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
class MyHashMap:

    def __init__(self):
        self.d=[Node(-1,-1) for i in range(0,10000)]
    
    def hash(self,key):
        return key%len(self.d)
        
    def put(self, key: int, value: int) -> None:
        curr=self.d[self.hash(key)]
        while curr.next!=None:
            if curr.next.key==key:
                curr.next.val=value
                return
            curr=curr.next
        curr.next=Node(key,value)
        
    def get(self, key: int) -> int:
        curr=self.d[self.hash(key)]
        while curr!=None:
            if curr.key==key:
                return curr.val
            curr=curr.next
        return -1

    def remove(self, key: int) -> None:
        curr=self.d[self.hash(key)]
        while curr.next:
            if curr.next.key==key:
                curr.next=curr.next.next
                return 
            curr=curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)