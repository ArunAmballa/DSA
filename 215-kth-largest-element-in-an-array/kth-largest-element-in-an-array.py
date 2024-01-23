import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for i in range(k):
            h.append(nums[i])
        heapq.heapify(h)
        for i in range(k,len(nums)):
            if nums[i]>h[0]:
                heapq.heapreplace(h,nums[i])
        return h[0]
