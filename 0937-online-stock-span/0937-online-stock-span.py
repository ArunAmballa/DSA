from queue import LifoQueue
class StockSpanner:

    def __init__(self):
        self.st=LifoQueue()
        

    def next(self, price: int) -> int:
        if self.st.empty():
            self.st.put([price,1])
            return 1
        else:
            cnt=1
            while not self.st .empty() and self.st.queue[-1][0]<=price:
                val,count=self.st.get()
                cnt=cnt+count
            self.st.put([price,cnt])
            return cnt
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)