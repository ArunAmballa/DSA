import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]
        self.median=-(1<<31)
        

    def addNum(self, num: int) -> None:
        if len(self.minHeap)==len(self.maxHeap):
            if num>self.median:
                heapq.heappush(self.minHeap,num)
                self.median=self.minHeap[0]
            else:
                heapq.heappush(self.maxHeap,-num)
                self.median=abs(self.maxHeap[0]) if self.maxHeap[0]<0 else -self.maxHeap[0]
        elif len(self.minHeap)>len(self.maxHeap):
            if num>self.median:
                topElement=heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap,-topElement)
                heapq.heappush(self.minHeap,num)
                top1=abs(self.maxHeap[0]) if self.maxHeap[0]<0 else -self.maxHeap[0]
                top2=self.minHeap[0]
                self.median=(top1+top2)/2
            else:
                heapq.heappush(self.maxHeap,-num)
                top1=abs(self.maxHeap[0]) if self.maxHeap[0]<0 else -self.maxHeap[0]
                top2=self.minHeap[0]
                self.median=(top1+top2)/2
        else:
            if num>self.median:
                heapq.heappush(self.minHeap,num)
                top1=abs(self.maxHeap[0]) if self.maxHeap[0]<0 else -self.maxHeap[0]
                top2=self.minHeap[0]
                self.median=(top1+top2)/2
            else:
                topElement=heapq.heappop(self.maxHeap)
                if topElement<0:
                    topElement=abs(topElement)
                else:
                    topElement=-topElement
                heapq.heappush(self.minHeap,topElement)
                heapq.heappush(self.maxHeap,-num)
                top1=abs(self.maxHeap[0]) if self.maxHeap[0]<0 else -self.maxHeap[0]
                top2=self.minHeap[0]
                self.median=(top1+top2)/2

        

    def findMedian(self) -> float:
        return self.median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()