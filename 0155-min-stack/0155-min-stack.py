from queue import LifoQueue
class MinStack:

    def __init__(self):
        self.st=LifoQueue()
        self.min=math.inf
        

    def push(self, val: int) -> None:
        self.min=min(self.min,val)
        self.st.put([val,self.min])
        
        
        

    def pop(self) -> None:
        value,mininum=self.st.get()
        if not self.st.empty():
            self.min=self.st.queue[-1][1]
        else:
            self.min=math.inf
        return value
        

    def top(self) -> int:
        return self.st.queue[-1][0]
        
        

    def getMin(self) -> int:
        return self.st.queue[-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()