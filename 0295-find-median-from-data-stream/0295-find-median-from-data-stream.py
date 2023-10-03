import heapq
class MedianFinder:

    def __init__(self):
        self.median=0
        self.min=[]
        self.max=[]

    def addNum(self, num: int) -> None:
        if len(self.min)==len(self.max):
            if num>self.median:
                heapq.heappush(self.min,num)
                self.median=self.min[0]
            else:
                heapq.heappush(self.max,-(num))
                self.median=abs(self.max[0]) if self.max[0]<0 else -(self.max[0])
        elif len(self.max)>len(self.min):
            if num>self.median:
                heapq.heappush(self.min,num)
                self.median=((abs(self.max[0]) if self.max[0]<0 else -(self.max[0]))+self.min[0])/2
            else:
                maxTop=heapq.heappop(self.max)
                maxTop=abs(maxTop) if maxTop<0 else -(maxTop)
                heapq.heappush(self.min,maxTop)
                heapq.heappush(self.max,-(num))
                self.median=((abs(self.max[0]) if self.max[0]<0 else -(self.max[0]))+self.min[0])/2
        else:
            if num<self.median:
                heapq.heappush(self.max,-(num))
                self.median=((abs(self.max[0]) if self.max[0]<0 else -(self.max[0]))+self.min[0])/2
            else:
                minTop=heapq.heappop(self.min)
                heapq.heappush(self.max,-(minTop))
                heapq.heappush(self.min,num)
                self.median=((abs(self.max[0]) if self.max[0]<0 else -(self.max[0]))+self.min[0])/2

        

    def findMedian(self) -> float:
        return self.median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()