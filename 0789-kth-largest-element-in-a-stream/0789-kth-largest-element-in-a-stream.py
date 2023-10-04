import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.h=[]
        count=0
        i=0
        while i<len(nums):
            heapq.heappush(self.h,nums[i])
            count=count+1
            i=i+1
            if count==self.k:
                break
        while i<len(nums):
            if nums[i]>self.h[0]:
                heapq.heapreplace(self.h,nums[i])
            i=i+1
    def add(self, val: int) -> int:
        if len(self.h)!=self.k:
            heapq.heappush(self.h,val)
        else:
            if val>self.h[0]:
                heapq.heapreplace(self.h,val)
        return self.h[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)