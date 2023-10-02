class Node:
    def __init__(self,key,value):
        self.key=key 
        self.val=value 
        self.next=None
class MyHashMap:

    def __init__(self):
        self.map=[Node(-1,-1) for i in range(1000)]
        
    def hash(self,key):
        return key%1000

    def put(self, key: int, value: int) -> None:
        curr=self.map[self.hash(key)]
        temp=curr
        while curr!=None:
            if curr.key==key:
                curr.val=value
                return
            curr=curr.next
        newNode=Node(key,value)
        newNode.next=temp.next
        temp.next=newNode
    
    def get(self, key: int) -> int:
        curr=self.map[self.hash(key)]
        while curr!=None:
            if curr.key==key:
                return curr.val
            curr=curr.next
        return -1

    def remove(self, key: int) -> None:
        curr=self.map[self.hash(key)]
        while curr!=None:
            if curr.next==None:
                return
            if curr.next.key==key:
                curr.next=curr.next.next
            curr=curr.next
    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)