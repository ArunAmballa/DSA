class MyCircularDeque:

    def __init__(self, size: int):
        self.size=size
        self.arr=[-1]*size
        self.front=-1
        self.rear=-1
        

    def insertFront(self, val: int) -> bool:
        #Overflow
        #Empty
        #CircularNature
        #NormalFlow
        if((self.front==0 and self.rear==self.size-1) or (self.rear==self.front-1)):
            return False
        elif(self.front==-1 and self.rear==-1):
            self.front=self.front+1 
            self.rear=self.rear+1 
            self.arr[self.front]=val
            return True
        elif(self.front==0 and self.rear!=self.size-1):
            self.front=self.size-1
            self.arr[self.front]=val
            return True
        else:
            self.front=self.front-1 
            self.arr[self.front]=val
            return True

    def insertLast(self, val: int) -> bool:
        #Overflow
        #Empty
        #CircularNature
        #NormalFlow
        if((self.front==0 and self.rear==self.size-1) or (self.rear==self.front-1)):
            return False
        elif(self.front==-1 and self.rear==-1):
            self.front=self.front+1 
            self.rear=self.rear+1 
            self.arr[self.rear]=val
            return True
        elif(self.rear==self.size-1 and self.front!=0):
            self.rear=0
            self.arr[self.rear]=val
            return True
        else:
            self.rear=self.rear+1 
            self.arr[self.rear]=val
            return True

    def deleteFront(self) -> bool:
        #underflow
        #SingleElement
        #CircularNature
        #NormalFlow
        if(self.front==-1 and self.rear==-1):
            return False
        elif(self.front==self.rear):
            self.arr[self.front]=-1
            self.front=-1
            self.rear=-1
            return True
        elif(self.front==self.size-1):
            self.arr[self.front]=-1
            self.front=0
            return True
        else:
            self.arr[self.front]=-1
            self.front=self.front+1
            return True

    def deleteLast(self) -> bool:
        #underflow
        #SingleElement
        #CircularNature
        #NormalFlow
        if(self.front==-1 and self.rear==-1):
            return False
        elif(self.front==self.rear):
            self.arr[self.rear]=-1
            self.front=-1
            self.rear=-1
            return True
        elif(self.rear==0):
            self.arr[self.rear]=-1
            self.rear=self.size-1
            return True
        else:
            self.arr[self.rear]=-1
            self.rear=self.rear-1
            return True

    def getFront(self) -> int:
        if self.front==-1 and self.rear==-1:
            return -1
        return self.arr[self.front]
        

    def getRear(self) -> int:
        if self.front==-1 and self.rear==-1:
            return -1
        return self.arr[self.rear]
        

    def isEmpty(self) -> bool:
        return self.front==-1 and self.rear==-1
        

    def isFull(self) -> bool:
        if((self.front==0 and self.rear==self.size-1) or (self.rear==self.front-1)):
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()