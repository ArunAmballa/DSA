from queue import Queue
class MyStack:

    def __init__(self):
        self.queue=Queue()
        

    def push(self, x: int) -> None:
        self.queue.put(x)
        for i in range(self.queue.qsize()-1):
            self.queue.put(self.queue.get())
        return

        

    def pop(self) -> int:
        return self.queue.get()
        

    def top(self) -> int:
        return self.queue.queue[0]
        

    def empty(self) -> bool:
        return self.queue.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()