import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h=[]
        for i in range(len(piles)):
            heapq.heappush(h,-piles[i])

        for i in range(k):
            maxi=abs(heapq.heappop(h))
            maxi=maxi-math.floor(maxi//2)
            heapq.heappush(h,-maxi)
        return abs(sum(h))
