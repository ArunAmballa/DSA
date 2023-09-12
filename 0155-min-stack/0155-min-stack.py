from queue import LifoQueue
class MinStack:

    def __init__(self):
        self.st=LifoQueue()
        

    def push(self, val: int) -> None:
        if self.st.empty():
            self.st.put([val,val])
        else:
            self.st.put([val,min(val,self.st.queue[-1][1])])
        

    def pop(self) -> None:
        value,minimum=self.st.get()
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