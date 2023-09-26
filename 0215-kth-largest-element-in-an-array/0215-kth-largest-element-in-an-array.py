import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for i in range(0,k):
            heapq.heappush(h,nums[i])
        for i in range(k,len(nums)):
            if nums[i]>h[0]:
                heapq.heapreplace(h,nums[i])
        return h[0]