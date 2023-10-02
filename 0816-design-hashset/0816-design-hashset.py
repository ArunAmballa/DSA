class Node:
    def __init__(self,key):
        self.key=key 
        self.next=None
class MyHashSet:

    def __init__(self):
        self.set=[Node(-1) for i in range(1000)]
        
    def hash(self,key):
        return key%1000

    def add(self, key: int) -> None:
        curr=self.set[self.hash(key)]
        temp=curr
        while curr!=None:
            if curr.key==key:
                return
            curr=curr.next
        newNode=Node(key)
        newNode.next=temp.next
        temp.next=newNode

    def remove(self, key: int) -> None:
        curr=self.set[self.hash(key)]
        while curr!=None:
            if curr.next==None:
                return
            if curr.next.key==key:
                curr.next=curr.next.next
            curr=curr.next

        

    def contains(self, key: int) -> bool:
        curr=self.set[self.hash(key)]
        while curr!=None:
            if curr.key==key:
                return True
            curr=curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)