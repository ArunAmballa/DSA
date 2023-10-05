class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        h=[]
        for i in d:
            if len(h)<k:
                heapq.heappush(h,(d[i],i))
            elif len(h)==k:
                if d[i]>h[0][0]:
                    heapq.heapreplace(h,(d[i],i))
        ans=[]
        while h:
            frequency,element=heapq.heappop(h)
            ans.append(element)
        return ans
        